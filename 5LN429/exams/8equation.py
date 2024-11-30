
def f8(x):
    result = 0
    for i in x:
        result += (i - 2)
    total = result / 2
    return total
print(f8([4,2,1,2]))