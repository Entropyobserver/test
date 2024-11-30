def factorials(n: int) -> dict:
    result = {}
    fact = 1
    for i in range(1, n+1):
        fact *= i
        result[i] = fact
    return result