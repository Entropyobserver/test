import operator
def get_lines(path):
    f = open(path,'r')
    lines = f.readlines()
    f.close()
    return lines
def get_lexicon(path):
    lexicon_words = []
    lines = get_lines(path)
    for line in lines:
        line = line.strip()
        lexicon_words.append(line)
    return lexicon_words
def is_vowel(char):
    vowels = "aeiouyåäö"
    lower_char = char.lower()
    if lower_char in vowels:
        return True
    else:
        return False
def get_vowel_count(str):
    count = 0
    for char in str:
        if is_vowel(char):
            count += 1
    return count
def get_word_vowels(words):
    word_vowel_dict = {}
    for word in words:
        vowel_count = get_vowel_count(word)
        word_vowel_dict[word] = vowel_count
    return word_vowel_dict
def get_token_vowels(tokens, vowel_dict):
    token_vowel_counts = []
    for token in tokens:
        if token in vowel_dict:
            vowel_count = vowel_dict[token]
        else:
            vowel_count = 0
        token_vowel_counts.append(vowel_count)
    return token_vowel_counts
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
from math import sqrt

def get_stdev(numbers):
    n = len(numbers)
    if n <= 1:
        return 0
    mean = get_mean(numbers)
    
    total_var = 0
    for number in numbers:
        variance = (number - mean) ** 2
        total_var += variance

    variance_mean = total_var / (n - 1)
    stdev = sqrt(variance_mean)
    return stdev

def main():
    #lexicon_file = 'D:/J/Desktop/language technology/programming-5LN429/assignment_2/sv-utf8.txt'
    #sentence_file = 'D:/J/Desktop/language technology/programming-5LN429/assignment_2/swe-sentences.txt'
    lexicon_file = 'sv-utf8.txt'
    sentence_file = 'swe-sentences.txt'
    lexicon_words = get_lexicon(lexicon_file)
    word_vowel_counts = get_word_vowels(lexicon_words)
    sentences = get_lines(sentence_file)
    
    tokens = []
    for line in sentences:
        words_in_line = line.split()
        for word in words_in_line:
            tokens.append(word)
    
    token_vowel_counts = get_token_vowels(tokens, word_vowel_counts)
    
    mean = get_mean(token_vowel_counts)
    stdev = get_stdev(token_vowel_counts)
    print("Mean of the text:", mean)
    print("Std of the text:", stdev)    
    
if __name__ == "__main__":
    main()
