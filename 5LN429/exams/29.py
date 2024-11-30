def f9(n):
    if n % 5 == 2:
        return True
    return False

def g9(L):
    nums = []
    for e in L:
        if f9(e):
            nums.append(e)
    return nums

print(sum(g9([2, 4, 6, 8, 10, 12, 22])))
