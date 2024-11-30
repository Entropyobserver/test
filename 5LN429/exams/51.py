def f1(x):
    y = []
    for i in range(len(x)):
        if x[i] > 3:
            y.append(x[i] - i)
    return y

numbers = [2, 3, 5, 7, 11]
print(f1(numbers))
