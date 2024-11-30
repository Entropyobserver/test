import nltk
from nltk import word_tokenize
from math import log
import csv
import json

# Ensure NLTK resources are downloaded
nltk.download('punkt', quiet=True)

def get_lines(file_path):
    """
    Read lines from a file and return them as a list of strings.
    
    :param file_path: Path to the input file
    :return: List of lines from the file
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def get_unigrams(lines):
    """
    Generate unigram frequency dictionary from input lines.
    
    :param lines: List of input strings
    :return: Dictionary of unigrams and their frequencies
    """
    unigram_counts = {}
    for line in lines:
        words = word_tokenize(line.strip().lower())
        words = ['<s>'] + words + ['<e>']
        for word in words:
            word = word.strip()
            unigram_counts[word] = unigram_counts.get(word, 0) + 1
    return unigram_counts

def get_bigrams(lines):
    """
    Generate bigram frequency dictionary from input lines.
    
    :param lines: List of input strings
    :return: Dictionary of bigrams and their frequencies
    """
    bigram_counts = {}
    for line in lines:
        words = word_tokenize(line.strip().lower())
        words = ['<s>'] + words + ['<e>']
        for i in range(len(words) - 1):
            first_word = words[i].strip()
            second_word = words[i + 1].strip()
            bigram = (first_word, second_word)
            bigram_counts[bigram] = bigram_counts.get(bigram, 0) + 1
    return bigram_counts

def get_surprisal(probability):
    """
    Calculate surprisal from a given probability.
    
    :param probability: Probability value
    :return: Surprisal value
    """
    return -log(probability, 2)

def get_bigram_surprisal(unigram_dict, bigram_dict):
    """
    Calculate surprisal for bigrams based on unigram and bigram frequencies.
    
    :param unigram_dict: Dictionary of unigram frequencies
    :param bigram_dict: Dictionary of bigram frequencies
    :return: Dictionary of bigrams with their surprisal values
    """
    bi_sur_dict = {}
    for bi_word, bigram_count in bigram_dict.items():
        first_word, second_word = bi_word
        unigram_count = unigram_dict.get(first_word, 0)
        
        # Smoothing logic
        unigram_count_smooth = unigram_count + len(bigram_dict)
        bigram_count_smooth = bigram_count + 1
        
        # Conditional probability
        cond_p = bigram_count_smooth / unigram_count_smooth
        
        # Calculate surprisal
        s = get_surprisal(cond_p)
        bi_sur_dict[bi_word] = s
    
    return bi_sur_dict

def get_test_surprisal(sentence, unigram_dict, bigram_dict):
    """
    Calculate average surprisal for a given sentence.
    
    :param sentence: Input sentence
    :param unigram_dict: Dictionary of unigram frequencies
    :param bigram_dict: Dictionary of bigram frequencies
    :return: Average surprisal of the sentence
    """
    words = word_tokenize(sentence.strip().lower())
    surprisal_values = []
    
    for i in range(1, len(words)):
        prev_word = words[i - 1].strip()
        current_word = words[i].strip()
        
        unigram_count = unigram_dict.get(prev_word, 0)
        bigram_count = bigram_dict.get((prev_word, current_word), 0)
        
        # Smoothing logic
        unigram_count_smooth = unigram_count + len(bigram_dict)
        bigram_count_smooth = bigram_count + 1
        
        # Conditional probability
        cond_p = bigram_count_smooth / unigram_count_smooth
        
        # Calculate surprisal
        surprisal = get_surprisal(cond_p)
        surprisal_values.append(surprisal)
    
    # Return average surprisal
    return sum(surprisal_values) / len(surprisal_values) if surprisal_values else 0

def main():
    """
    Main function to process text and calculate surprisal.
    """
    # Paths to input files
    training_path = r'D:\J\Desktop\language technology\s\5LN715\ans2\wiki.train.raw'
    test_path = r'D:\J\Desktop\language technology\s\5LN715\ans2\merged.txt'
    
    # Read training lines
    training_lines = get_lines(training_path)
    
    # Get unigram and bigram frequencies
    unigram_dict = get_unigrams(training_lines)
    bigram_dict = get_bigrams(training_lines)
    
    # Calculate bigram surprisal
    bigram_surprisal = get_bigram_surprisal(unigram_dict, bigram_dict)
    
    # Read and process test sentence
    test_sentences = get_lines(test_path)
    
    # Load durations
    with open(r'D:\J\Desktop\language technology\s\5LN715\ans2\durations.json', 'r') as f:
        durations = json.load(f)
    
    # Process each test sentence
    results = []
    for sentence in test_sentences:
        # Calculate surprisal for each sentence
        avg_surprisal = get_test_surprisal(sentence, unigram_dict, bigram_dict)
        print(f"Sentence: {sentence.strip()}")
        print(f"Average Surprisal: {avg_surprisal}")
        
        # Detailed word-level surprisal and duration
        words = word_tokenize(sentence.strip().lower())
        for i in range(1, len(words)):
            prev_word = words[i - 1].strip()
            current_word = words[i].strip()
            
            unigram_count = unigram_dict.get(prev_word, 0)
            bigram_count = bigram_dict.get((prev_word, current_word), 0)
            
            unigram_count_smooth = unigram_count + len(bigram_dict)
            bigram_count_smooth = bigram_count + 1
            
            cond_p = bigram_count_smooth / unigram_count_smooth
            word_surprisal = get_surprisal(cond_p)
            
            duration = durations.get(current_word, 0)
            
            results.append((current_word, duration, word_surprisal))
    
    # Write results to CSV
    with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Word', 'Duration', 'Surprisal'])
        writer.writerows(results)

if __name__ == "__main__":
    main()