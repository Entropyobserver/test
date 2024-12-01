import re, sys

# Define a function that takes as input a filepath and that returns
#the lines of that file. Use the method .readlines()
def read_line(path):
    with open(path,'r',encoding = 'utf-8') as f:
        lines = f.readlines()
        return lines

def main():
    # Add code for a function call here. Pass in sys.argv[1] to the function.
    #path = '/home/yaxi4987/5LN701/lab01/dev1-raw.txt'
    path = sys.argv[1]
    lines = read_line(path)
    for line in lines:
        for token in re.split("\s+", line.strip()):
            print(token)
"""
\s is a regular expression that matches any whitespace character (spaces, tabs, newlines).
The + quantifier means "one or more" of the preceding element. So \s+ matches one or more whitespace characters.
Therefore, re.split("\s+", line.strip()) will split the stripped line into tokens wherever there are one or more whitespace characters.
"""
main()

#python nlp5LN701tokenizer0.py '/home/yaxi4987/5LN701/lab01/dev1-raw.txt'
#python3 nlp5LN701tokenizer0.py '/home/yaxi4987/5LN701/lab01/dev1-raw.txt' > '/home/yaxi4987/5LN701/lab01/dev0-tok.txt'
#python3 score-tokens.py dev1-gold.txt dev3-tok.txt

#Precision = 0.9207317073170732 (755/820)Recall = 0.8324145534729879 (755/907)F-score = 0.8743485813549507