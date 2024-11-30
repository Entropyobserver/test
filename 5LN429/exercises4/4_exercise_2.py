"""
    Define a function is_prime() that takes one parameter as input.
    The function will have a try-except. Try to convert the input argument
    to an integer. Return None in the except if the type of the input is not
    an integer. However, if the input is a prime number, the function should
    return True, else False.

    What is a prime number? A prime number is a natural number greater than 1
    that has no positive divisors other than 1 and itself. Thus, 2, 3, 5, 7,
    and 11 are all examples of prime numbers, whereas 4, 6, 9, 12, 14, and 15
    all are examples of numbers that are not primes. 

    Hint: Use modulo % to solve this exercise.

    The rest of the program should be as follows.

    Define a function main() that takes no arguments. Inside main(), is_prime()
    is assigned to a variable. Pass in sys.argv[1]. In order to use sys, put
    this in the beginning of the code:

import sys 

    Lastly, in main(), print the Boolean.

    Remember to call main()

    To run the code, you need to pass in an argument. For example, you can
    pass in 5:

python3 solution2.py 5

    The program should print True if you pass in a prime, otherwise False.


import sys
def is_prime_1(x):
    try:
        if x % x == 0:
            x = int(x)
    except ValueError:
            return None
def main():
    result = is_prime_1(sys.argv[1])
    print(result)
if __name__ == "__main__":
    main()

import sys

def is_prime_2(n):
    try:
        n = int(n)   
        if n <= 1:
            return False
        for i in range(2,n):
            if n % i == 0:
                return False
        return True
    except ValueError:
        return None

def main():
    result = is_prime_2(sys.argv[1])
    print(result)
if __name__ == "__main__":
    main()
"""
import sys
def is_prime_3(n):
    try:
        n = int(n)
    except ValueError:
        return None
    if n <= 1:
        return False
        for i in range(2,n):
            if n % i == 0:
                return False
    return True

#def main():
    #result = is_prime_3(sys.argv[1])
    #print(result)
#if __name__ == "__main__":
    #main()


