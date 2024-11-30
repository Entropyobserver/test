def f5(a, b, c):
    if a > b:
        if a > c:
            return a
    else:
        if b < c:
            return b
        else:
            return c

print(f5(1, 2, 3))
print(f5(1, 3, 2))
print(f5(2, 1, 3))
print(f5(2, 3, 1))
print(f5(3, 1, 2))
print(f5(3, 2, 1))
