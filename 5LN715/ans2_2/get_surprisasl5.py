import nltk
from nltk import word_tokenize
from math import log
import csv
import json

# Ensure NLTK resources are downloaded
nltk.download('punkt', quiet=True)

def get_lines(training_path):
    """
    Read lines from a file and return them as a list of strings.
    """
    with open(training_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def get_unigrams(lines):
    """
    Generate unigram frequency dictionary from input lines.
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
    """
    bigram_counts = {}
    for line in lines:
        words = word_tokenize(line.strip().lower())
        words = ['<s>'] + words + ['<e>']
        for i in range(len(words) - 1):
            bigram = (words[i].strip(), words[i + 1].strip())
            bigram_counts[bigram] = bigram_counts.get(bigram, 0) + 1
    return bigram_counts

def get_surprisal(probability):
    """
    Calculate surprisal from a given probability.
    """
    return -log(probability, 2) if probability > 0 else float('inf')

def get_bigram_surprisal(unigram_dict, bigram_dict):
    """
    Calculate surprisal for bigrams based on unigram and bigram frequencies.
    """
    bi_sur_dict = {}
    vocab_size = len(unigram_dict)  # Vocabulary size for smoothing
    for bi_word, bigram_count in bigram_dict.items():
        first_word, second_word = bi_word
        unigram_count = unigram_dict.get(first_word, 0)
        
        # Smoothing
        unigram_count_smooth = unigram_count + vocab_size
        bigram_count_smooth = bigram_count + 1
        
        # Conditional probability
        cond_p = bigram_count_smooth / unigram_count_smooth
        
        # Calculate surprisal
        bi_sur_dict[bi_word] = get_surprisal(cond_p)
    
    return bi_sur_dict

def get_test_surprisal(sentence, unigram_dict, bigram_dict):
    """
    Calculate average surprisal for a given sentence.
    """
    words = ['<s>'] + word_tokenize(sentence.strip().lower()) + ['<e>']
    surprisal_values = []
    
    for i in range(1, len(words)):
        prev_word = words[i - 1]
        current_word = words[i]
        
        unigram_count = unigram_dict.get(prev_word, 0)
        bigram_count = bigram_dict.get((prev_word, current_word), 0)
        
        # Smoothing
        unigram_count_smooth = unigram_count + len(unigram_dict)
        bigram_count_smooth = bigram_count + 1
        
        # Conditional probability
        cond_p = bigram_count_smooth / unigram_count_smooth
        
        # Calculate surprisal
        surprisal_values.append(get_surprisal(cond_p))
    
    return sum(surprisal_values) / len(surprisal_values) if surprisal_values else 0

def main():
    """
    Main function to process text and calculate surprisal.
    """
    # Paths to input files
    training_path = r'D:\J\Desktop\language technology\course\5LN715\ans2\wiki.train.raw'
    test_path = r'D:\J\Desktop\language technology\s\5LN715\ans2\merged.txt'
    
    # Read training lines
    print("Loading training data...")
    training_lines = get_lines(training_path)
    
    # Get unigram and bigram frequencies
    print("Building unigram and bigram models...")
    unigram_dict = get_unigrams(training_lines)
    bigram_dict = get_bigrams(training_lines)
    
    # Read and process test sentences
    print("Processing test sentences...")
    test_sentences = get_lines(test_path)
    
    # Load word durations
    with open(r'D:\J\Desktop\language technology\s\5LN715\ans2\durations.json', 'r') as f:
        durations = json.load(f)
    
    # Results list
    results = []
    for sentence in test_sentences:
        # Calculate surprisal for the sentence
        avg_surprisal = get_test_surprisal(sentence, unigram_dict, bigram_dict)
        print(f"Sentence: {sentence.strip()}")
        print(f"Average Surprisal: {avg_surprisal:.6f}")
        
        # Word-level surprisal and duration
        words = ['<s>'] + word_tokenize(sentence.strip().lower()) + ['<e>']
        for i in range(1, len(words)):
            prev_word = words[i - 1]
            current_word = words[i]
            
            unigram_count = unigram_dict.get(prev_word, 0)
            bigram_count = bigram_dict.get((prev_word, current_word), 0)
            
            # Smoothing
            unigram_count_smooth = unigram_count + len(unigram_dict)
            bigram_count_smooth = bigram_count + 1
            
            cond_p = bigram_count_smooth / unigram_count_smooth
            word_surprisal = get_surprisal(cond_p)
            
            duration = durations.get(current_word, 0)
            
            results.append((current_word, duration, word_surprisal))
    
    # Write results to CSV
    print("Writing results to output5.csv...")
    with open('output5.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Word', 'Duration', 'Surprisal'])
        writer.writerows(results)

    print("Processing complete.")

if __name__ == "__main__":
    main()
