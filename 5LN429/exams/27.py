def f7(a, b):
    L = []
    for i in a:
        try:
            x = int(i)
            if x in b:
                L.append(x)
        except:
            L.append(g7(i))
    return L[:-3]

def g7(y):
    c = 0
    for e in y:
        c += 1
    return c

L1 = [1, "Newton", "9", "left", 0, "the", "ghost", "intact", "2"]
L2 = ["9", "1", 1, "ghost", 2]

print(f7(L1, L2))
