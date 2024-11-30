def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

while True:
    number = int(input("Please type in a number: "))
    if number <= 0:
        print("Thanks and bye!")
        break
    else:
        print(f"The factorial of the number {number} is {factorial(number)}")