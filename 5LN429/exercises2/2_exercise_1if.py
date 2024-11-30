"""

    Write a function smaller_than_100() that takes one parameter.
    (An integer when you call the function.)
    The function should return True if the number is smaller than
    100, otherwise 

    False

"""
def smaller_than_100(x):
    if x < 100:
        return True
    else:
        return False
print(smaller_than_100(110))

def smaller_than_100(x):
    return x < 100