"""
def count_chars(string):
    n = 0
    for char in string:
        n += 1
    return n
def main():
    print(count_chars('hello'))
main()
"""
def count_chars(string):
    n = 0
    print("Step 1: Initialize n to 0")
    print(f"Initial value of n: {n}")
    for char in string:
        n += 1
        print(f"Step 2: Iterate through character: {char}, increment n")
        print(f"Current value of n: {n}")
    return n

def main():
    result = count_chars('hello')
    print("Step 3: Function call completed")
    print(f"Final result: {result}")

main()