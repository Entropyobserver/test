from math import sqrt
from collections import defaultdict
import string

def get_lines(path):
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        return lines

def get_lexicon(path):
    lexicon_words = []
    lines = get_lines(path)
    for line in lines:
        line = line.strip()
        lexicon_words.append(line)
    return lexicon_words

def is_vowel(char):
    char = char.lower()
    if char in 'aeiouyåäö':
        return True
    else: 
        return False

def get_vowel_count(word):
    count = 0
    for char in word:
        if is_vowel(char):
            count += 1
    return count

def get_word_vowels(words):
    word_vowel_dict = {}
    for word in words:
        vowel_count = get_vowel_count(word)
        word_vowel_dict[word] = vowel_count
    return word_vowel_dict

def get_token_vowels(tokens, word_vowel_dict):
    result = []
    for token in tokens:
        cleaned_token = ''
        for char in token:
            if char not in string.punctuation:
                cleaned_token += char.lower()
        if cleaned_token:
            vowel_count = word_vowel_dict.get(cleaned_token, get_vowel_count(cleaned_token))
            result.append(vowel_count)
    return result

def get_mean(lst):
    total = 0
    count = 0
    for number in lst:
        total += number
        count += 1
    if count == 0:
        return 0
    else:
        return total / count

def get_stdev(numbers):
    mean = get_mean(numbers)
    var = sum((number - mean) ** 2 for number in numbers) / (len(numbers) - 1)
    return sqrt(var)

def main():
    lexicon = get_lexicon('sv-utf8.txt')
    #lexicon = get_lexicon('D:/J/Desktop/language technology/programming-5LN429/assignment_2/sv-utf8.txt')
    word_vowel_dict = get_word_vowels(lexicon)
    
    lines = get_lines('swe-sentences.txt')
    #lines = get_lines('D:/J/Desktop/language technology/programming-5LN429/assignment_2/swe-sentences.txt')
   
    tokens = []
    for line in lines:
        words = line.split()
        for word in words:
            tokens.append(word)
    vowel_counts = get_token_vowels(tokens, word_vowel_dict)
    
    mean = get_mean(vowel_counts)
    stdev = get_stdev(vowel_counts)
    
    print('Mean of syllables:', mean)
    print('Standard deviation of syllables',stdev)

if __name__ == '__main__':
    main()
