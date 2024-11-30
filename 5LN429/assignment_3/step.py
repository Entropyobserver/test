import sys
from collections import defaultdict

def get_lines(path):
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        return lines

def get_lexicon(path):
    lexicon = []
    lines = get_lines(path)
    for line in lines:
        line = line.strip()
        lexicon.append(line)
    return lexicon

#lexicon = get_lexicon('sv-utf8.txt')
#print(len(lexicon))
#print(lexicon[:10])

def get_sorted(lst):
#    sorted_lst = lst.sort(ascending = True)
    sorted_lst = sorted(lst)
    return sorted_lst
#sorted_lst = get_sorted(lexicon)
#print(sorted_lst[:20])

def get_dict(lexicon):
    anagram_dict = defaultdict(list)
    for word in lexicon:
        sorted_word = ''.join(get_sorted(word))
        anagram_dict[sorted_word].append(word)
    return anagram_dict

def get_anagram(anagram_dict,input_word):
    sorted_input_word = ''.join(sorted(input_word))
    anagram_lst = []
    for word in anagram_lst[sorted_input_word]:
        if word != input_word:
            anagram_lst.append(word)
    return anagram_lst
#anagram = get_anagram(sorted_lst,word)
#print(anagram)


def main():
    lexicon = get_lexicon('sv-utf8.txt')
    anagram_dict = get_dict(lexicon)
    input_word = sys.argv[1]
    anagrams = get_anagram(anagram_dict,input_word)
    for i in anagrams:
        print(i)