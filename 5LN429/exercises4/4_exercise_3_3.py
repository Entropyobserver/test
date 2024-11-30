import sys

def get_lines(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        return lines
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def get_word_frequency(lines):
    word_freq = {}
    for line in lines:
        words = line.strip().lower().split()
        for word in words:
            word = ''.join(e for e in word if e.isalpha())  # remove non-alphabetic characters
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
        words = line.split()
        for word in words:
            word = word.strip().lower()
            complexity = cal_complexity(word, word_freq)
            total_complexities += complexity
            total_words += 1
    readability = total_complexities / total_words
    return readability

def main():
    if len(sys.argv)!= 3:
        print("Usage: python script.py <en_file> <chomsky_file>")
        sys.exit(1)

    en_file = sys.argv[1]
    chomsky_file = sys.argv[2]

    en_lines = get_lines(en_file)
    freq_dict = get_word_frequency(en_lines)
    chomsky_lines = get_lines(chomsky_file)
    readability = cal_readability(chomsky_lines, freq_dict)
    print(f"Readability: {readability:.2f}")

if __name__ == "__main__":
    main()