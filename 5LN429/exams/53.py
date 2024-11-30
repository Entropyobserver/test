"""
Write only a function f3 ( ) that takes a list of strings as a parameter, The function should return adictionary 
where each key is a string longer than five characters, and each value is the length of thatstring. Make sure no 
punctuation is included as part of the keys or counted as characters. Include the following as the last lines and 
show the output:
chomsky_quote = "If we don't believe in freedom of expression for people we despise, wedon't believe in it at all".split()
print(f3(chomsky_quote))
"""


import string

def f3(words):
    # Create a dictionary for words longer than five characters with their lengths
    result = {}
    for word in words:
        # Remove punctuation and check word length
        cleaned_word = word.strip(string.punctuation)
        if len(cleaned_word) > 5:
            result[cleaned_word] = len(cleaned_word)
    return result

# Test the function
chomsky_quote = "If we don't believe in freedom of expression for people we despise, we don't believe in it at all".split()
print(f3(chomsky_quote))
