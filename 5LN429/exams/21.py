def f1(n, m):
    if n > m:
        return True
    if m > n:
        return False
    return g1(n,m)

def g1(x, y):
    return sum(((x+y)*2,x+y))
print(f1(3,4))
print(f1(4,3))
print(f1(3,3))