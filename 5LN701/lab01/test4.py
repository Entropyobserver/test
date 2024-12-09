import re
def tokenize(text):
    pattern = r"(?:\w+\.\w+\.(?:\w+)*)"
    #pattern = r"(?:[a-zA-Z]\.)+"
    tokens = re.findall(pattern, text)
    return tokens
text = "The meeting is on Nov. 10. Abbreviations like Ph.D., V.I.P., and U.S. are handled."
tokens = tokenize(text)
print(tokens)  
# ['Ph.D.', 'V.I.P', 'U.S.']