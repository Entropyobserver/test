import sys

def is_prime_3(n):
    try:
        n = int(n)
        print(f"Converted input to integer: {n}")
    except ValueError:
        print("Input is not a valid integer.")
        return None

    if n <= 1:
        print(f"{n} is not a prime number (<= 1).")
        return False

    for i in range(2, n):
        if n % i == 0:
            print(f"{n} is divisible by {i}, so it is not a prime number.")
            return False

    print(f"{n} is a prime number.")
    return True

def main():
    if len(sys.argv) < 2:
        print("No input provided. Please provide a number as a command line argument.")
        return

    result = is_prime_3(sys.argv[1])
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
