import re
text = "30-day post-chaise year-end pianist-comedian short-term"
pattern = r'\w+(?:-\w+)*'
tokens = re.findall(pattern, text)
print(tokens)  # Output: ['30-day', 'post-chaise', 'year-end', 'pianist-comedian', 'short-term']


import re
def tokenize(text):
    # Define the pattern to match words, numbers, and special cases like $30.50
    pattern = r'\b\w+(?:-\w+)*\b|\$\d+\.\d+|[%#$“”.,:;!?‘’]'
    tokens = re.findall(pattern, text)
    return tokens
# Example input
text = "The price is $30.50"
tokens = tokenize(text)
print(tokens)  # Output: ['The', 'price', 'is', '$30.50']

import re
def tokenize(text):
    pattern = r"(?:\wW+\.\w+\.(?:\w+)*)"
    tokens = re.findall(pattern, text)
    return tokens
text = "The meeting is on Nov. 10. Abbreviations like Ph.D., V.I.P., and U.S. are handled."
tokens = tokenize(text)
print(tokens)  
# ['Ph.D.', 'V.I.P', 'U.S.']




import re
def tokenize(text):
    text = re.sub(r"\b(\w+)n't\b", r"\1 n't ", text)  # can't, haven't
    text = re.sub(r"\b(\w+)'s\b", r"\1 's ", text)    # it's, he's
    tokens = text.split()
    return tokens
text = "It can't be true. I haven't eaten yet."
tokens = tokenize(text)
print(tokens)

import re
def tokenize(text):
    #pattern = "\b\w+(?:'\w+)?\b
    #pattern = r"\b\w+'t\b"
    pattern ="(?:\b\w+'t\b)"
    tokens = re.findall(pattern, text)
    return tokens
text = "It can't be true.I haven't eaten yet. "
tokens = tokenize(text)
print(tokens)  
# Output: 