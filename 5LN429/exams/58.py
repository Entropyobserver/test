def f8(X):
    # 计算每个元素平方的和
    sum_of_squares = 0
    sum_of_elements = 0
    for x in X:
        sum_of_squares += x**2
        # 初始化 sum_of_elements 并计算元素的总和
        sum_of_elements += x
    
    # 计算 M(X)
    M = sum_of_squares * sum_of_elements
    return M
print(f8([1,2,3]))