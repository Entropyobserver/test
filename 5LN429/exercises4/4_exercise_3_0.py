import math
import sys

def get_lines(path):
    with open(path, "r") as f:
        return f.readlines()

def get_clean(word):
    return word.lower().strip(".,!?()")

def get_word_freq(lines):
    word_freq = {}
    for line in lines:
        tokens = line.split()
        for w in tokens:
            word = get_clean(w)
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
    return word_freq

def get_adjacency(word, vowels, consonants):
    adjacent = 0
    for i in range(len(word) - 1):
        if word[i] in vowels and word[i + 1] in vowels:
            adjacent += 1
        elif word[i] in consonants and word[i + 1] in consonants:
            adjacent += 1
    return adjacent

def get_adj_len(lines, vowels, consonants):
    word_scores = {}
    for line in lines:
        for word in line.split():
            word = get_clean(word)
            adj = get_adjacency(word, vowels, consonants)
            adj_len = adj + len(word)
            word_scores[word] = adj_len
    return word_scores

def get_readability(word_scores, word_freq):
    combined = []
    for word, score in word_scores.items():
        freq = word_freq.get(word, 1)  # default to 1 if word not found
        readability = score / freq
        combined.append(readability)
    return sum(combined) / len(combined)

def main():
    data_path = sys.argv[1]
    lines_path = sys.argv[2]

    data = get_lines(data_path)
    lines = get_lines(lines_path)

    vowels = "aeiouy"
    consonants = "bcdfghjklmnpqrstvwxz"

    word_freq = get_word_freq(data)
    word_score = get_adj_len(lines, vowels, consonants)

    readability = get_readability(word_score, word_freq)
    print(readability)

main()
