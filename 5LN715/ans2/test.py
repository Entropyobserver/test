import math
import re
from collections import Counter

def get_lines(filepath):
    """
    Read lines from a file.
    
    Args:
        filepath (str): Path to the text file
    
    Returns:
        list: Lines in the file
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: File {filepath} not found.")
        return []

def get_unigrams(lines):
    """
    Get unigram frequencies from lines.
    
    Args:
        lines (list): List of text lines
    
    Returns:
        dict: Unigram frequencies
    """
    # Tokenize lines into words
    words = [word.lower() for line in lines for word in re.findall(r'\w+', line)]
    return dict(Counter(words))

def get_bigrams(lines):
    """
    Get bigram frequencies from lines.
    
    Args:
        lines (list): List of text lines
    
    Returns:
        dict: Bigram frequencies
    """
    bigrams = []
    for line in lines:
        words = re.findall(r'\w+', line.lower())
        bigrams.extend(list(zip(words[:-1], words[1:])))
    return dict(Counter(bigrams))

def get_surprisal(probability):
    """
    Calculate surprisal from probability.
    
    Args:
        probability (float): Probability of an event
    
    Returns:
        float: Surprisal value
    """
    if probability <= 0:
        return float('inf')
    return -math.log2(probability)

def get_bigram_surprisal(unigrams, bigrams):
    """
    Calculate surprisal for bigrams.
    
    Args:
        unigrams (dict): Unigram frequencies
        bigrams (dict): Bigram frequencies
    
    Returns:
        dict: Bigram surprisal values
    """
    total_words = sum(unigrams.values())
    
    bigram_surprisals = {}
    for (w1, w2), count in bigrams.items():
        # Probability calculation: P(w2|w1) = count(w1,w2) / count(w1)
        unigram_prob = unigrams.get(w1, 1) / total_words
        bigram_prob = count / unigrams.get(w1, 1)
        
        bigram_surprisals[(w1, w2)] = get_surprisal(bigram_prob)
    
    return bigram_surprisals

def get_test_surprisal(sentence, unigrams, bigrams):
    """
    Calculate average surprisal for a sentence.
    
    Args:
        sentence (str): Sentence to analyze
        unigrams (dict): Unigram frequencies
        bigrams (dict): Bigram frequencies
    
    Returns:
        float: Average surprisal
    """
    words = re.findall(r'\w+', sentence.lower())
    
    if len(words) < 2:
        return 0
    
    surprisals = [get_surprisal(bigrams.get((words[i], words[i+1]), 1) / 
                                unigrams.get(words[i], 1)) 
                  for i in range(len(words)-1)]
    
    return sum(surprisals) / len(surprisals)

def main():
    """
    Main function to demonstrate surprisal calculations.
    """
    filepath = 'corpus.txt'  # Default filepath
    
    lines = get_lines(filepath)
    unigrams = get_unigrams(lines)
    bigrams = get_bigrams(lines)
    
    # Example sentences for testing
    test_sentences = [
        "This is a test sentence",
        "Natural language processing is fascinating",
        "Surprisal calculation helps understand language"
    ]
    
    print("Unigram Frequencies (Top 10):")
    print(dict(sorted(unigrams.items(), key=lambda x: x[1], reverse=True)[:10]))
    
    print("\nBigram Frequencies (Top 10):")
    print(dict(sorted(bigrams.items(), key=lambda x: x[1], reverse=True)[:10]))
    
    print("\nTest Sentence Surprisals:")
    for sentence in test_sentences:
        avg_surprisal = get_test_surprisal(sentence, unigrams, bigrams)
        print(f"'{sentence}': {avg_surprisal:.2f}")

if __name__ == "__main__":
    main()