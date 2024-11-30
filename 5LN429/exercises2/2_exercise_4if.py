"""
    Write a function is_larger_than_10() that takes one parameter. 
    Return None if the input argument is not an integer.
    Return True if the argument is larger than 10, otherwise False.

"""
def is_larger_than_10(x):
    if not isinstance(x,int):
        return None
    if x > 10:
        return True
    else:
        return False
print(is_larger_than_10("hi"))

print(is_larger_than_10(20))
print(is_larger_than_10(5))


