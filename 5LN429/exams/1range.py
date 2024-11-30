def f1(x):
    y = []
    for i in range(x):
        for j in range(i):
            y.append(i-j)
    return y
print(f1(3))