import sys
from collections import defaultdict

def get_lines(path):
    print(f"Reading file: {path}")
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            print(f"First 20 lines from {path}:")
            print("".join(lines[:20]))
            return lines
    except FileNotFoundError:
        print(f"Error: File {path} not found.")
        sys.exit(1)

def get_lexicon(path):
    print("Creating lexicon...")
    lexicon = [line.strip() for line in get_lines(path)]
    print("First 20 words in lexicon:")
    print(lexicon[:20])
    return lexicon

def get_dict(lexicon):
    print("Creating anagram dictionary...")
    anagram_dict = defaultdict(list)
    for word in lexicon:
        sorted_word = ''.join(sorted(word))
        anagram_dict[sorted_word].append(word)
    print("First 20 entries in anagram dictionary:")
    print(list(anagram_dict.items())[:20])
    return anagram_dict

def get_anagram(anagram_dict, input_word):
    print(f"Searching for anagrams of '{input_word}'...")
    sorted_input_word = ''.join(sorted(input_word))
    if sorted_input_word in anagram_dict:
        anagrams = [word for word in anagram_dict[sorted_input_word] if word != input_word]
        print(f"Found {len(anagrams)} anagram(s).")
        return anagrams
    print("No anagrams found.")
    return []

def main():
    if len(sys.argv) < 2:
        print("Error: Please provide an input word as a command line argument.")
        sys.exit(1)

    print("Starting program...")
    lexicon = get_lexicon('sv-utf8.txt')
    anagram_dict = get_dict(lexicon)
    input_word = sys.argv[1]
    print(f"Input word: {input_word}")
    anagrams = get_anagram(anagram_dict, input_word)

    if anagrams:
        print("Anagrams found:")
        for i in anagrams:
            print(i)
    else:
        print(f"No anagrams found for '{input_word}'.")

if __name__ == '__main__':
    main()