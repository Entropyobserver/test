def get_sorted(lst):
    sorted_lst = sorted(lst)
    return sorted_lst
words = ["safweg","wege","ewgewg"]
print(get_sorted(words))
sorted_word = ''.join(get_sorted(words))
print(sorted_word)


from collections import defaultdict

anagram_dict = defaultdict(list)
for word in words:
    sorted_word = ''.join(get_sorted(word))
    anagram_dict[sorted_word].append(word)
print(anagram_dict)