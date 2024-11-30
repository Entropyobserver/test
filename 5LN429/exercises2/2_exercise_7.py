"""
    Write a function max_out_of_three() that takes three integers as input
    and returns the largest input. If the numbers are equal, return any.

    For example:
    
    max_out_of_three(5,6,7)
    max_out_of_three(7,5,6)
    max_out_of_three(5,7,6)
    max_out_of_three(7,7,7)


   should all return 7

"""
def max_out_of_three(x,y,z):
    if x == y == z:
        return x
    else:
        return max((x,y,z))
print(max_out_of_three(5,6,7))
print(max_out_of_three(7,5,6))
print(max_out_of_three(5,7,6))
print(max_out_of_three(7,7,7))
