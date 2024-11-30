from math import sqrt
from collections import defaultdict

def get_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def get_lexicon(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file]

def is_vowel(char):
    return char.lower() in 'aeiouåäö'

def get_vowel_count(word):
    return sum(1 for char in word if is_vowel(char))

def get_word_vowels(words):
    return {word: get_vowel_count(word) for word in words}

def get_token_vowels(text, word_vowels):
    return [word_vowels.get(token.lower(), get_vowel_count(token)) for token in text]

def get_mean(values):
    return sum(values) / len(values)

def get_stdev(values):
    mean = get_mean(values)
    variance = sum((x - mean) ** 2 for x in values) / (len(values) - 1)
    return sqrt(variance)

def main():
    lexicon = get_lexicon('sv-utf8.txt')
    word_vowels = get_word_vowels(lexicon)
    
    lines = get_lines('swe-sentences.txt')
    tokens = [token for line in lines for token in line.split()]
    
    token_vowels = get_token_vowels(tokens, word_vowels)
    
    mean_syllables = get_mean(token_vowels)
    stdev_syllables = get_stdev(token_vowels)
    
    print(f"Mean number of syllables: {mean_syllables:.2f}")
    print(f"Standard deviation of syllables: {stdev_syllables:.2f}")

if __name__ == "__main__":
    main()
