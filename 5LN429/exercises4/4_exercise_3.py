"""
    In this exercise, you will write a program that prints the readability
    of a text, where the readability is a rough measure that I came up
    with just for this exercise -- in other words, I don't know whether
    it is a good measure. It probably is not, because it does only operate
    on word level and does not take into account sentence length or complexity.

    Try your best write code that is modularized -- that is, use functions,
    and read up on PEP8 to follow the conventions. For example, you will have
    to get the lines from two different files, so define a function to
    open those files and get the lines instead of repeating 
    code (DRY). Furthermore, remember the single-responsibility principle:
    Try to structure your code so that each function solves one task.

    OK. But what is readability in this exercise?

    To get the readability, take the sum all of words' complexity,
    and divide that sum by the total number of words, in a text. The complexity
    of a word is defined as follows:

    complexity = (adjacency + word length) / word frequency

    where adjacency of a word is the number of times two vowels are adjacent to
    one another plus the number of times two consonants are adjacent
    to one another, where word length is the number of characters
    in the word, and word frequency comes from a separate text.

    Example of adjacency for a few words:
    
    linguistic -> 3 (because ng = 1, ui = 1, st = 1)
    theory -> 2 (because th = 1, eo = 1)
    the -> 1 (because th = 1)
    in -> 0 

    Populate a dictionary where each word is a key and the word's frequency is
    the value. Use the file UNv1.0.testset.en for this dictionary.
    Remember to use lower case and to strip away punctuation.

    When you have the adjacancy and length, you can access the word
    frequencies from the dictionary using .get()
    The method .get() returns None if the word is not in the dictionary.
    Since you cannot divide by None, use 1 instead.

    Measure the readability of this file:

chomsky_1965_aspects_excerpt.txt

    Use sys to pass in the files. Here is an example of how to use sys:


import sys

un_file = sys.argv[1]
chomsky_file = sys.argv[2]


    Remember that sys.argv returns a list of arguments to the command
    python, where index 0 is the .py, file. Hence, here is the full command
    you will run:


python 4-ans-3.py UNv1.0.testset.en chomsky_1965_aspects_excerpt.txt


    Desired output:


3.9722734146246084

    (And yes, it is irritating that "command" is ambiguous.)
    
"""
import sys
def get_lines(path):
    with open(path,'r',encoding='utf-8') as f:
        lines = f.readlines()
    return lines

def get_word_frequency(lines):
    word_freq = {}
    for line in lines:
        words = line.strip().lower().split()
        for word in words:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
    return word_freq

def cal_adjacency(word):
    adjacency = 0
    vowels = 'aeiou'
    for i in range(len(word) - 1):
        if (word[i] in vowels and  word[i+1] in vowels) or \
        (word[i] not in vowels and word[i+1] not in vowels):
            adjacency += 1
    return adjacency

def cal_complexity(word,word_freq):
    adjacency = cal_adjacency(word)
    word_length = len(word)
    freq = word_freq.get(word,1)
    complexity = (adjacency + word_length) / freq
    return complexity

def cal_readability(lines,word_freq):
    total_complexities = 0
    total_words = 0
    for line in lines:
        words = line.split()
        for word in words:
            word = word.strip().lower()
            complexity = cal_complexity(word,word_freq)
            total_complexities += complexity
            total_words += 1
    readability = total_complexities / total_words
    return readability

def main():
    en = sys.argv[1]
    chomsky = sys.argv[2]

    en_lines = get_lines(en)
    freq_dict = get_word_frequency(en_lines)
    chomsky_lines = get_lines(chomsky)
    readability = cal_readability(chomsky_lines,freq_dict)
    print(readability)

if __name__ == "__main__":
    main()
