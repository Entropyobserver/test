"""

    Write a function get_log_n() that takes one parameter.
    The function should return the logarithm of that input number. Use 

import math

n = 8

math.log(n, 2)

    where n is your input argument, and 2 is to get log_2

    Outside the function, write a for-loop that goes from 1 to 9.
    (Not including 9.)
    Inside the for-loop, print a call of the function and pass in
    the loop variable.

    The output should be:

0.0
1.0
1.5849625007211563
2.0
2.321928094887362
2.584962500721156
2.807354922057604
3.0

"""
import math   
def get_log_n(n):
    return math.log(n,2)
i = 0
for i in range(1,10):

    print(get_log_n(i))




#x = 1

#for i in range(9):
#    print i
