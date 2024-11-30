"""
    Write code for a function get_squares_of_even() that takes two arguments
    n and m, and returns a list of the squares of even numbers in range(n,m)

    Use list comprehension.

    Test case:

print(get_squares_of_even(2,13))

    Output should be:

[4, 16, 36, 64, 100, 144]

"""
def get_squares_of_even(n,m):
    return [i**2 for i in range(n,m) if i % 2 == 0]
print(get_squares_of_even(2,13))