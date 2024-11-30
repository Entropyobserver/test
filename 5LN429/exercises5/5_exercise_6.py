""" 

    Write a function that returns True if the argument to that function
    is an email address that have a string of length between 3 and 7 
    characters, followed by a full stop, followed by a string of length
    between 3 and 7 characters, followed by an at-sign @, followed by
    full stop, followed by the string 'mail', followed
    by one of the following strings:

    com
    org
    se

    Otherwise, the function should return False.
    All strings must be lower case. Use regexp.
    
    Some test cases:

print(is_email("john.doe@mail.com"))
print(is_email("jo.doe@mail.org"))
print(is_email("maryjane.watson@mail.org"))

    This should output:

True
False
False

"""
import re
def is_email(str):
    #pattern = r"^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$"
    pattern = r"^[a-z]{3,7}\.[a-z]{3,7}@mail\.(com|org|se)$"
    match = re.search(pattern,str)
    return bool(match)

print(is_email("john.doe@mail.com"))
print(is_email("jo.doe@mail.org"))
print(is_email("maryjane.watson@mail.org"))

import re


def is_email(string):
    pattern = r"[a-z]{3,7}\.[a-z]{3,7}@mail\.com|org|se"
    if re.match(pattern,string):
        return True
    return False


def main():
    print(is_email("john.doe@mail.com"))
    print(is_email("jo.doe@mail.org"))
    print(is_email("maryjane.watson@mail.org"))


main()