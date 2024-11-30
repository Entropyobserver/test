def f2(m, n):
    counter = 5
    while m < n:
        m += 4
        n += 2
        counter += 1
    return counter

print(f2(5, 8))
