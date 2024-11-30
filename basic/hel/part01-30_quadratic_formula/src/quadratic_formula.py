
"""
# Write your solution here
# Let's take the square root of math-module in use
from math import sqrt
a = float(input("Value of a:"))
b = float(input("Value of b:"))
c = float(input("Value of c:"))
delta = b**2-4*a*c
x1 = (-b + sqrt(b**2-4*a*c))/(2*a)
x2 = (-b - sqrt(b**2-4*a*c))/(2*a)
# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5
"""
# Let's take the square root from the math module
from math import sqrt

# Input values for a, b, and c
a = float(input("Value of a: "))
b = float(input("Value of b: "))
c = float(input("Value of c: "))

# Calculate the discriminant
delta = b**2 - 4*a*c

# Calculate the roots
if delta > 0:
    print("delta is greater than 0")
    x1 = (-b + sqrt(delta)) / (2*a)
    x2 = (-b - sqrt(delta)) / (2*a)
    print(f"The roots are {x1} and {x2}")
elif delta == 0:
    print("delta equals to 0")
    x1 = x2 = -b / (2*a)
    print(f"The root is {x1}")
else:
    print("delta is smaller than 0")
    real_part = -b / (2*a)
    imaginary_part = sqrt(-delta) / (2*a)
    print(f"The roots are {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i")

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5