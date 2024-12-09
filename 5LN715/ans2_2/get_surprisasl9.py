
import nltk
from nltk import word_tokenize
from math import log
import csv
import json

nltk.download('punkt', quiet=True)

def get_lines(file_path):
    """
    param: file_path: Input file path
    return: List of file lines
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def get_unigrams(lines):
    """
    Generate unigram(word) frequency dictionary from input lines
    param: List of input strings
    return: Dictionary of words and their frequencies
    """
    unigram_counts = {}
    for line in lines:
        # Tokenize and convert to lowercase
        words = word_tokenize(line.strip().lower())
        # Add sentence start and end markers
        words = ['<s>'] + words + ['<e>']
        for word in words:
            word = word.strip()
            unigram_counts[word] = unigram_counts.get(word, 0) + 1
    return unigram_counts

def get_bigrams(lines):
    """
    Generate bigram (word pair) frequency dictionary from input lines
    param:List of input strings
    return: Dictionary of word pairs and their frequencies
    """
    bigram_counts = {}
    for line in lines:
        # Tokenize and convert to lowercase
        words = word_tokenize(line.strip().lower())
        # Add sentence start and end markers
        words = ['<s>'] + words + ['<e>']
        for i in range(len(words) - 1):
            first_word = words[i].strip()
            second_word = words[i + 1].strip()
            bigram = (first_word, second_word)
            bigram_counts[bigram] = bigram_counts.get(bigram, 0) + 1
    return bigram_counts

def get_surprisal(probability):
    """
    Calculate surprisal based on probability (-log2(p))
    param:Probability value
    return: Surprisal value
    """
    return -log(probability, 2)

def get_test_surprisal(sentence, unigram_dict, bigram_dict, durations):
    """
    Calculate the average surprisal of a test sentence based on unigram and bigram frequencies
    param sentence: Input sentence
    param unigram_dict: Unigram dictionary from training data
    param bigram_dict: Bigram dictionary from training data
    param durations: Dictionary of word durations
    return: Average surprisal of the sentence, and surprisal and duration of each word
    """
    V = len(unigram_dict)  # Vocabulary size
    words = word_tokenize(sentence.strip().lower())
    words = ['<s>'] + words + ['<e>']
    
    total_surprisal = 0
    word_count = 0
    word_results = []
    
    for i in range(1, len(words)):
        prev_word = words[i - 1].strip()
        current_word = words[i].strip()
        
        # Get unigram count of the previous word
        unigram_count = unigram_dict.get(prev_word, 0)
        
        # Get bigram count of the previous word and the current word
        bigram_count = bigram_dict.get((prev_word, current_word), 0)
        
        # Estimate probability using Laplace smoothing
        unigram_count_smooth = unigram_count + V
        bigram_count_smooth = bigram_count + 1
        
        # Calculate conditional probability using Laplace smoothing
        if unigram_count == 0:
            cond_p = 1 / V
        else:
            cond_p = bigram_count_smooth / unigram_count_smooth
        
        # Calculate surprisal
        word_surprisal = get_surprisal(cond_p)
        
        # Get word duration
        duration = durations.get(current_word, 0)
        
        # Record word results
        word_results.append((current_word, duration, word_surprisal))
        
        total_surprisal += word_surprisal
        word_count += 1
    
    # Return average surprisal and word-level results
    avg_surprisal = total_surprisal / word_count if word_count > 0 else 0
    return avg_surprisal, word_results

def main():
    """
    Main function to process text and calculate surprisal
    """
    # Input file paths (please modify according to actual situation)
    training_path = r'D:\J\Desktop\language technology\course\ans2 copy\wiki.train.raw'  # Training data path
    test_path = r'D:\J\Desktop\language technology\course\ans2 copy\sentence_15.txt'  # Test sentence path
    
    # Read training data
    training_lines = get_lines(training_path)
    
    # Get unigram and bigram frequencies
    unigram_dict = get_unigrams(training_lines)
    bigram_dict = get_bigrams(training_lines)
    
    # Read test sentences
    test_sentences = get_lines(test_path)
    
    # Load word durations from JSON file
    try:
        with open('D:\\J\\Desktop\\language technology\\course\\ans2 copy\\duration15.json', 'r') as f:
            durations = json.load(f)
    except FileNotFoundError:
        print("Duration file not found, using default duration 0")
        durations = {}
    
    # Process each test sentence
    sentence_results = []
    all_word_results = []
    
    for sentence in test_sentences:
        # Calculate average surprisal and word-level results for the sentence
        avg_surprisal, word_results = get_test_surprisal(sentence, unigram_dict, bigram_dict, durations)
        
        # Record sentence results
        sentence_results.append((sentence.strip(), avg_surprisal))
        all_word_results.extend(word_results)
        
        # Print results
        print(f"Sentence: {sentence.strip()}")
        print(f"Average Surprisal: {avg_surprisal}\n")
        
        print("Word Results:")
        for word, duration, surprisal in word_results:
            print(f"Word: {word}, Duration: {duration}, Surprisal: {surprisal}")

    
    # Write results to CSV files
    with open('output_sentences15.csv', 'w', newline='', encoding='utf-8') as csvfile:
        sentence_writer = csv.writer(csvfile)
        sentence_writer.writerow(['Sentence', 'Average Surprisal'])
        sentence_writer.writerows(sentence_results)
    
    with open('output_words15.csv', 'w', newline='', encoding='utf-8') as csvfile:
        word_writer = csv.writer(csvfile)
        word_writer.writerow(['Word', 'Duration', 'Surprisal'])
        word_writer.writerows(all_word_results)

if __name__ == "__main__":
    main()
