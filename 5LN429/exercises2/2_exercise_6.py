"""
    Write a program that has two functions. 

    The first function times_five() should take one parameter,
    check that it is an integer, and return that number times five. 

    The second function also_times_five() should also take one parameter
    and check if it is an integer, and if it is, call the first function,
    passing in the input to the second function and returning that times five.

    For example, also_times_five(5) should return 125

"""
def times_five(x):
    return 5*x
def also_times_five(y):
    if isinstance(y,int):
        return times_five(y)*5
print(also_times_five(5))
