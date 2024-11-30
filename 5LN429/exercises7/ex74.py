"""

    Write a function get_uneven_indecies() that takes a list of numbers
    as an input argument. Then use enumerate and list comprehension
    to return a list of booleans corresponding to if the index of the
    number is odd.

    Test case:

nums = [1, 2, 3, 4, 5]
print(get_uneven_indecies(nums))

    Output:

[False, True, False, True, False]



def get_uneven_indecies(lst):
    return [bool(num) for num in lst if num % 2 != 0]
nums = [1, 2, 3, 4, 5]
print(get_uneven_indecies(nums))

def get_uneven_indecies(lst):
    return [bool(index) for index,num in enumerate(lst) if index % 2 != 0] 
nums = [1, 2, 3, 4, 5]
print(get_uneven_indecies(nums))
"""
def get_uneven_indecies(lst):
    return [index % 2 != 0 for index, _ in enumerate(lst)]
nums = [1, 2, 3, 4, 5]
print(get_uneven_indecies(nums))
