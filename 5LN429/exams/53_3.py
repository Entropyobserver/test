import string

def f4(lst):
    result = {}
    for word in lst:
        cleaned_word = word.strip(string.punctuation)
        if len(cleaned_word) >= 3 and len(cleaned_word) % 2 == 1:
            result[cleaned_word] = cleaned_word[::-1]
    return result

example_quote = "To be or not to be, that is the question".split()
print(f4(example_quote))
