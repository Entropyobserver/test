"""

    Write a Python function that takes a string as input and checks
    if it contains at least one digit. Use a regular expression.

    Possible test cases:

print(has_digit("666"))
print(has_digit("foobar"))


    Output should be:

True
False

"""
import re
def has_digit_match(str):
   # pattern = r"\d[0-9]"
    pattern = r"\d"
    match = re.match(pattern,str)
    return bool(match)

print(has_digit_match("666"))
print(has_digit_match("foobar"))

def has_digit_findall(str):
   # pattern = r"\d[0-9]"
    pattern = r"\d"
    findall = re.findall(pattern,str)
    return bool(findall)

print(has_digit_match("666"))
print(has_digit_match("foobar"))

import re


def has_digit(s):
    pattern = r"[0-9]"
    if re.match(pattern,s):
        return True
    return False

print(has_digit("666"))
print(has_digit("foobar"))



