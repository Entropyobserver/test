from math import sqrt
from collections import defaultdict

def get_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def get_lexicon(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().split()

def is_vowel(char):
    return char.lower() in 'aeiouyåäö'

def get_vowel_count(word):
    return sum(1 for char in word if is_vowel(char))

def get_word_vowels(words):
    return {word: get_vowel_count(word) for word in words}

def get_token_vowels(tokens, word_vowel_dict):
    return [word_vowel_dict.get(token, 0) for token in tokens]

def get_mean(values):
    return sum(values) / len(values)

def get_stdev(values):
    mean = get_mean(values)
    variance = sum((x - mean) ** 2 for x in values) / (len(values) - 1)
    return sqrt(variance)

def main():
    lexicon = get_lexicon('sv-utf8.txt')
    word_vowel_dict = get_word_vowels(lexicon)
    
    lines = get_lines('swe-sentences.txt')
    tokens = [word for line in lines for word in line.split()]
    vowel_counts = get_token_vowels(tokens, word_vowel_dict)
    
    mean_vowels = get_mean(vowel_counts)
    stdev_vowels = get_stdev(vowel_counts)
    
    print(f'Mean number of syllables: {mean_vowels}')
    print(f'Standard deviation of syllables: {stdev_vowels}')

if __name__ == '__main__':
    main()

