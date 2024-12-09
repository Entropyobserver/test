from nltk import sent_tokenize, word_tokenize
from collections import defaultdict
from math import log
import sys, time
import csv
import json
import nltk
# nltk.download('punkt') 

def get_lines(file_path):
    """
    param: file_path: Input file path
    return: List of file lines
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def get_unigrams(sentences):
    unigram_dict = {}
    for sentence in sentences:
        words = word_tokenize(sentence)
        words = [word.lower() for word in words]
        words = ['<s>'] + words + ['<e>']
        for word in words:
            if word in unigram_dict:
                unigram_dict[word] += 1
            else:
                unigram_dict[word] = 1
    return unigram_dict

def get_bigrams(sentences):
    bigram_dict = {}
    for sentence in sentences:
        words = word_tokenize(sentence)
        words = [word.lower() for word in words]
        words = ['<s>'] + words + ['<e>']
        for i in range(len(words) - 1):
            bi_word = (words[i], words[i + 1])
            if bi_word in bigram_dict:
                bigram_dict[bi_word] += 1
            else:
                bigram_dict[bi_word] = 1
    return bigram_dict

def get_surprisal(p):
    s = -log(p, 2)
    return s

def get_bigram_surprisal(unigram_dict, bigram_dict):
    bi_sur_dict = {}
    V = len(unigram_dict)  # Vocabulary size including all unigrams in the training set
    
    # Improved smoothing logic
    for bi_word in bigram_dict:
        first_word, second_word = bi_word
        unigram_count = unigram_dict.get(first_word, 0)
        bigram_count = bigram_dict.get(bi_word, 0)

        # More precise conditional probability calculation
        # Using Laplace smoothing, considering all possible words
        if unigram_count == 0:
            cond_p = 1 / V  # If the previous word does not exist, use uniform distribution
        else:
            # More complex smoothing formula
            cond_p = (bigram_count + 1) / (unigram_count + V)

        # Calculate surprisal with more detailed comments
        s = -log(cond_p, 2)  # Negative log probability to calculate surprisal
        bi_sur_dict[bi_word] = s

    return bi_sur_dict

def get_test_surprisal(sentence, bi_sur_dict, durations):
    """
    More accurately calculate the surprisal of a sentence using the precomputed bigram surprisal dictionary
    """
    words = word_tokenize(sentence.strip().lower())
    words = ['<s>'] + words + ['<e>']
    
    total_surprisal = 0
    word_count = 0
    word_results = []
    
    for i in range(1, len(words)):
        prev_word = words[i - 1].strip()
        current_word = words[i].strip()
        
        # Get surprisal from the precomputed dictionary
        # If not found, give a default high surprisal value
        word_surprisal = bi_sur_dict.get((prev_word, current_word), 
                                         # For unseen bigrams, give a large default surprisal value
                                         -log(1 / len(bi_sur_dict), 2) if bi_sur_dict else 10)
        
        # Get word duration
        duration = durations.get(current_word, 0)
        
        # Record word-level results
        word_results.append((current_word, duration, word_surprisal))
        
        total_surprisal += word_surprisal
        word_count += 1
    
    # Calculate average surprisal
    avg_surprisal = total_surprisal / word_count if word_count > 0 else 0
    return avg_surprisal, word_results

def main():
    # Input file paths (please modify according to actual situation)
    training_path = r'D:\J\Desktop\language technology\course\ans2 copy\wiki.train.raw'  # Training data path
    test_path = r'D:\J\Desktop\language technology\course\ans2 copy\sentence_1.txt'  # Test sentence path
    
    # Read training data
    training_lines = get_lines(training_path)
    
    # Get unigram and bigram frequencies
    unigram_dict = get_unigrams(training_lines)
    bigram_dict = get_bigrams(training_lines)
    
    # Read test sentences
    test_sentences = get_lines(test_path)
    
    # Load word durations from JSON file
    try:
        with open(r'D:\J\Desktop\language technology\course\ans2 copy\word_duration1.json', 'r', encoding='utf-8') as f:
            durations = json.load(f)
    except FileNotFoundError:
        print("Duration file not found, using default duration 0")
        durations = {}
    
    # Calculate bigram surprisal dictionary
    bi_sur_dict = get_bigram_surprisal(unigram_dict, bigram_dict)
    
    # Process each test sentence
    sentence_results = []
    all_word_results = []
    
    for sentence in test_sentences:
        # Use precomputed surprisal dictionary
        avg_surprisal, word_results = get_test_surprisal(sentence, bi_sur_dict, durations)
        
        # Record sentence results
        sentence_results.append((sentence.strip(), avg_surprisal))
        all_word_results.extend(word_results)
        
        # Print results
        print(f"Sentence: {sentence.strip()}")
        print(f"Average Surprisal: {avg_surprisal}\n")
        
        print("Word Results:")
        for word, duration, surprisal in word_results:
            print(f"Word: {word}, Duration: {duration}, Surprisal: {surprisal}")
    
    # Write sentence-level results to CSV file
    with open('output_sentences1.csv', 'w', newline='', encoding='utf-8') as csvfile:
        sentence_writer = csv.writer(csvfile)
        sentence_writer.writerow(['Sentence', 'Average Surprisal'])
        sentence_writer.writerows(sentence_results)
    
    # Write word-level results to CSV file
    with open('output_words1.csv', 'w', newline='', encoding='utf-8') as csvfile:
        word_writer = csv.writer(csvfile)
        word_writer.writerow(['Word', 'Duration', 'Surprisal'])
        for result in all_word_results:
            word_writer.writerow(result)

if __name__ == "__main__":
    main()
