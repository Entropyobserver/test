"""
    Write a function get_word_ids() that takes a string as input and
    returns a dictionary where keys are unique words in the string,
    and values are lists of indices where those words appear.
    Ignore punctuation and make use of .lower() to get all words in lower case.

    Here is the string that should be passed in. (A Franz Kafka quote.)

"I write differently from what I speak, I speak differently from what I think, I think differently from the way I ought to think, and so it all proceeds into deepest darkness."

    TIP: Use strip() to get rid of punctuation marks.
    
    Desired output:

{'i': [0, 5, 7, 12, 14, 20], 'write': [1], 'differently': [2, 9, 16], 'from': [3, 10, 17], 'what': [4, 11], 'speak': [6, 8], 'think': [13, 15, 23], 'the': [18], 'way': [19], 'ought': [21], 'to': [22], 'and': [24], 'so': [25], 'it': [26], 'all': [27], 'proceeds': [28], 'into': [29], 'deepest': [30], 'darkness': [31]}
"""
def get_word_ids_1(text):
    text = text.lower()
    text = text.strip(".")
    text = text.replace(",","")
    text = text.split()
    word_dict = {}
    for index,word in enumerate(text):
        if word in word_dict:
            word_dict[word].append(index)
        else:
            word_dict[word] = [index]
    return word_dict
t1 = "I write differently from what I speak, I speak differently from what I think, I think differently from the way I ought to think, and so it all proceeds into deepest darkness."
print(get_word_ids_1(t1))
from collections import defaultdict

def get_word_ids_2(text):
    text = text.lower()
    text = text.strip(".")
    text = text.replace(",","")
    text = text.split()
    word_dict = defaultdict(list)
    for index,word in enumerate(text):
            word_dict[word].append(index)
    return(word_dict)
t1 = "I write differently from what I speak, I speak differently from what I think, I think differently from the way I ought to think, and so it all proceeds into deepest darkness."
print(get_word_ids_2(t1))

import re
def get_word_ids_3(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]','',text)
    text = text.split()
    word_dict = defaultdict(list)
    for index,word in enumerate(text):
            word_dict[word].append(index)
    return(word_dict)
print("method 3 is running")
t1 = "I write differently from what I speak, I speak differently from what I think, I think differently from the way I ought to think, and so it all proceeds into deepest darkness."
import string
print(get_word_ids_3(t1))
def get_word_ids_4(text):
    text = text.lower()
    text = text.translate(str.maketrans('','',string.punctuation))
    text = text.split()

    word_dict = defaultdict(list)
    for index,word in enumerate(text):
            word_dict[word].append(index)
    return(word_dict)
print("method 4 is runnnig:")
print(get_word_ids_4(t1))
t1 = "I write differently from what I speak, I speak differently from what I think, I think differently from the way I ought to think, and so it all proceeds into deepest darkness."