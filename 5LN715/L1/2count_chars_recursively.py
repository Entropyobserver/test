
"""
def count_chars_recursively(string, n=0):
    try:
        string[n]
        n += 1
        return count_chars_recursively(string, n)
    except IndexError:
        return n

def main():
    print(count_chars_recursively('hello',5))
"""
def count_chars_recursively(string, n=0):
    try:
        print(f"Step 1: Checking character at index {n}")
        string[n]
        print(f"Step 2: Character at index {n} exists, incrementing n")
        n += 1
        return count_chars_recursively(string, n)
    except IndexError:
        print("Step 3: Reached the end of the string, returning n")
        return n

def main():
    result = count_chars_recursively('hello', 0)
    print(f"Final result: {result}")

main()