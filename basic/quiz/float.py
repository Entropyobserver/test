a = 0.1
b = 0.2 
c = 0.3
print(a + b == c)
#这是因为浮点数在计算机中并不是精确存储的。虽然我们期望 (0.1 + 0.2) 等于 (0.3)，但由于浮点数的表示方式，实际计算结果会有微小的误差。
#在 Python 中，(0.1 + 0.2) 的结果实际上是 (0.30000000000000004)，而不是精确的 (0.3)。

def fun(x):
    if x > 3:
        return x * fun(x-1) 
    else:
        return x
print(fun(6))

#fun(3) 返回 (3)
#fun(4) 返回 (4 \times 3 = 12)
#fun(5) 返回 (5 \times 12 = 60)
#fun(6) 返回 (6 \times 60 = 360)

num = range(1,11)
sliced_num = num[2:8]
result = sum(sliced_num) * 3
print(result)