import sys
from collections import defaultdict

def get_lines(path):
    print(f"Reading file: {path}")
    with open(path, "r") as f:
        lines = f.readlines()
    print(f"Lines read: {len(lines)}")
    return lines

def get_clean(word):
    print(f"Cleaning word: {word}")
    return word.lower().translate(str.maketrans('', '', '.,!?()'))

def get_word_freq(lines):
    print("Calculating word frequency...")
    word_freq = {}
    for line in lines:
        tokens = line.split()
        for w in tokens:
            word = get_clean(w)
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
    print("Word frequency calculated:")
    print(word_freq)
    return word_freq

def get_adjacency(word, vowels, consonants):
    print(f"Calculating adjacency for word: {word}")
    adjacent = 0
    for i in range(len(word) - 1):
        if word[i] in vowels and word[i + 1] in vowels:
            adjacent += 1
        elif word[i] in consonants and word[i + 1] in consonants:
            adjacent += 1
    print(f"Adjacency for {word}: {adjacent}")
    return adjacent

def get_adj_len(lines, vowels, consonants):
    print("Calculating adjacency and length for each word...")
    word_scores = {}
    for line in lines:
        for word in line.split():
            word = get_clean(word)
            adj = get_adjacency(word, vowels, consonants)
            adj_len = adj + len(word)
            print(f"Adjacency and length for {word}: {adj_len}")
            word_scores[word] = adj_len
    print("Adjacency and length calculated:")
    print(word_scores)
    return word_scores

def get_readability(word_scores, word_freq):
    print("Calculating readability...")
    combined = []
    for word, score in word_scores.items():
        freq = word_freq.get(word, 1)  # default to 1 if word not found
        readability = score / freq
        print(f"Readability for {word}: {readability}")
        combined.append(readability)
    print("Readability calculated:")
    print(combined)
    return sum(combined) / len(combined)

def main():
    if len(sys.argv)!= 3:
        print("Usage: python script.py <data_path> <lines_path>")
        return

    data_path = sys.argv[1]
    lines_path = sys.argv[2]

    try:
        data = get_lines(data_path)
        lines = get_lines(lines_path)
    except FileNotFoundError:
        print("File not found. Please check the file paths.")
        return

    vowels = "aeiouy"
    consonants = "bcdfghjklmnpqrstvwxz"

    word_freq = get_word_freq(data)
    word_score = get_adj_len(lines, vowels, consonants)

    readability = get_readability(word_score, word_freq)
    print(f"Final readability: {readability}")

if __name__ == '__main__':
    main()