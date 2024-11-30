"""

    For this one, we will not define any functions. Instead, assign to
    a variable a string that starts with a tab, and another raw string
    that starts with a tab. The idea of raw strings is that they take
    away the power of backslash \ in Python.

    Print both strings.

    Now an important distinction:
    
    The method re.match() from the beginning of a string.
    It stops when it finds a non-matching character or reaches
    the end of the string.

    The method re.search(), on the other hand, does not stop.

"""
import re
tab_string = "\tHello World"
raw_tab_string = r"\Hello World"
print(tab_string)
print(raw_tab_string)