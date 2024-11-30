"""
    Write a function that takes an integer as input.
    If the number is even, the function should return True, otherwise
    false.

def even(x):
    if x % 2 == 0:
        return True
    else:
        return False
print(even(7))
print(even(6))
"""
def even(x):
    return x % 2 == 0

print(even(7))
print(even(6))
