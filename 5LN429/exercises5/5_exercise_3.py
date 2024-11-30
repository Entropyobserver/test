"""
    
    Write a function that finds all the occurrences of the strings 'hello'
    and 'Hello' and returns a list of them.


    Some test cases:

text1 = "how are you? hello? can you hear me?"
text2 = "hello hello!"
text3 = "Hello! Hello! Hello hello!"

print(get_hello(text1))
print(get_hello(text2))
print(get_hello(text3))

    Output should be:

['hello']
['hello', 'hello']
['Hello', 'Hello', 'Hello', 'hello']


import re
def get_hello(str):
    pattern = r'\bhello\b'
    match = ''
    for char in str:
        if re.findall(pattern,str):
            return match

import re
def get_hello(str):
    pattern = r"hello"
    match =''
    if re.findall(pattern,str):
        return match
"""
import re
def get_hello(str):
    #pattern = r"[Hh]ello"
    pattern = r'\bhello\b|\bHello\b'
    match = re.findall(pattern,str)
    return match

text1 = "how are you? hello? can you hear me?"
text2 = "hello hello!"
text3 = "Hello! Hello! Hello hello!"

print(get_hello(text1))
print(get_hello(text2))
print(get_hello(text3))