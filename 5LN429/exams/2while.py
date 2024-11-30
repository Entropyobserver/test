def f2(m,n):
    counter = 0
    while m <= n:
        m *= 3
        n *= 2
        counter += 1
    return counter
print(f2(2,3))