import sys
import string

def get_lines(file_path):
    """Read lines from a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def create_frequency_dict(lines):
    """Create a word frequency dictionary from given lines."""
    freq_dict = {}
    for line in lines:
        words = line.lower().translate(str.maketrans('', '', string.punctuation)).split()
        for word in words:
            freq_dict[word] = freq_dict.get(word, 0) + 1
    return freq_dict

def calculate_adjacency(word):
    """Calculate adjacency for a word."""
    adjacency = 0
    vowels = set('aeiou')
    for i in range(len(word) - 1):
        if (word[i] in vowels and word[i+1] in vowels) or \
           (word[i] not in vowels and word[i+1] not in vowels):
            adjacency += 1
    return adjacency

def calculate_complexity(word, freq_dict):
    """Calculate complexity of a word."""
    adjacency = calculate_adjacency(word)
    word_length = len(word)
    frequency = freq_dict.get(word, 1)  # Use 1 if word not in dictionary
    return (adjacency + word_length) / frequency

def calculate_readability(text_lines, freq_dict):
    """Calculate readability of text."""
    total_complexity = 0
    word_count = 0
    for line in text_lines:
        words = line.lower().translate(str.maketrans('', '', string.punctuation)).split()
        for word in words:
            total_complexity += calculate_complexity(word, freq_dict)
            word_count += 1
    return total_complexity / word_count if word_count > 0 else 0

def main():
    #if len(sys.argv) != 3:
    #    print("Usage: python script.py UNv1.0.testset.en chomsky_1965_aspects_excerpt.txt")
    #    sys.exit(1)

    un_file = sys.argv[1]
    chomsky_file = sys.argv[2]

    un_lines = get_lines(un_file)
    freq_dict = create_frequency_dict(un_lines)

    chomsky_lines = get_lines(chomsky_file)
    readability = calculate_readability(chomsky_lines, freq_dict)

    print(f"{readability}")

if __name__ == "__main__":
    main()