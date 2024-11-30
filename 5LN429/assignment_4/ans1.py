"""
import math
def eq1(lst):
    n = len(lst)
    sum = 0
    for x in lst:
        sum += (x-x**3)**2*(n-1)/(math.sqrt(x))
    return sum
"""
import math
def eq1(x):
    n = len(x)
    sum = 0
    for i in range(min(13,n)):
        xi = x[i]
        if xi != 0:
            term = (xi - xi**3)**2 * (n-1) / math.sqrt(xi)
            sum += term
    return sum
print(eq1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))

def eq2(x):
    n = len(x)
    term = [((xi - xi**3)**2 * (n-1) / math.sqrt(xi)) for xi in range(min(13,n)) if xi != 0]
    return sum(term)
print(eq2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))