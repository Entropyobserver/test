
"""
    We have not yet talked about imports in Python.
    You can import libraries to not have to implement everything yourself.
    This should be avoided when learning how to code.
    But it is OK in certain cases.
    Type at the very beginning of your code:

    import math

    Your task is to print the number of decimal numbers in pi.
    Pi can be accessed with math.pi
    
    So if you do
    
    print(math.pi)

    the output should be:

    3.141592653589793

    Hint: Use str() to convert a float to a string.
    Use .split() to split a string into a list of items.

    This task can be done in one line, but that is probably harder.

    The output should be:

    15

"""
import math
x = str(math.pi)
x = x.split(".")
print(x[1][2:4])


