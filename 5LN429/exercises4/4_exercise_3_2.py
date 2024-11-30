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
        if (word[i] in vowels and word[i+1] in vowels) or \
        (word[i] not in vowels and word[i+1] not in vowels):
            adjacency += 1
    return adjacency

def cal_complexity(word, word_freq):
    adjacency = cal_adjacency(word)
    word_length = len(word)
    freq = word_freq.get(word, 1)
    complexity = (adjacency + word_length) / freq
    return complexity

def cal_readability(lines, word_freq):
    total_complexities = 0
    total_words = 0
    for line in lines:
        words = line.strip().lower().split()
        for word in words:
            word = ''.join(char for char in word if char.isalnum())  # Remove punctuation
            if word:  # Check if word is not empty after removing punctuation
                complexity = cal_complexity(word, word_freq)
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
    readability = cal_readability(chomsky_lines, freq_dict)
    print(readability)

if __name__ == "__main__":
    main()