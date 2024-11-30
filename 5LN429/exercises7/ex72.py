"""

    Write a function remove_vowels() that takes one argument, a list of words.
    The function should return a list with almost the same words, except that
    the vowels should be removed. Use list comprehension.
    
    Test case:

test = ["this", "is", "a", "sentence"]
print(remove_vowels(test))

    Output should be:

['ths', 's', '', 'sntnc']

"""
def remove_vowels(lst):
    vowels = 'aeiou'
    return [''.join([char for char in word if char.lower() not in vowels]) for word in lst]
test = ["this", "is", "a", "sentence"]
print(remove_vowels(test))