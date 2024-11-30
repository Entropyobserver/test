import sys
from collections import defaultdict

def get_lines(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"Error: File {path} not found.")
        sys.exit(1)

def get_lexicon(path):
    return [line.strip() for line in get_lines(path)]

def get_dict(lexicon):
    anagram_dict = defaultdict(list)
    for word in lexicon:
        sorted_word = ''.join(sorted(word))
        anagram_dict[sorted_word].append(word)
    return anagram_dict

def get_anagram(anagram_dict, input_word):
    sorted_input_word = ''.join(sorted(input_word))
    if sorted_input_word in anagram_dict:
        return [word for word in anagram_dict[sorted_input_word] if word != input_word]
    return []

def main():
    if len(sys.argv) < 2:
        print("Error: Please provide an input word as a command line argument.")
        sys.exit(1)

    lexicon = get_lexicon('sv-utf8.txt')
    anagram_dict = get_dict(lexicon)
    input_word = sys.argv[1]
    anagrams = get_anagram(anagram_dict, input_word)

    if anagrams:
        for i in anagrams:
            print(i)
    else:
        print(f"No anagrams found for '{input_word}'.")

if __name__ == '__main__':
    main()
