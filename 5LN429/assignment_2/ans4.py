def f4(lst):
    new_dict = {}
    for word in lst:
        new_dict[word] = len(word)
    return new_dict
#def f4_1(lst):
#    return {word: len(word) for word in lst}
#print(f4_1(['colorless', 'green', 'ideas', 'sleep', 'furiously']))
print(f4(['colorless', 'green', 'ideas', 'sleep', 'furiously']))

