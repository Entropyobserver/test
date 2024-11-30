
def f4(x, y):
    result = 1
    while x < y:
        x += 5
        y += 2
        result += x * 2
    return result

print(f4(3, 10))  