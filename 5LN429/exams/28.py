def f8(x):
    result = 0
    for i in x:
        result += i + 3
        total = result/3
    return total
print(f8([4,2,1,2]))