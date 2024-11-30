# what's the output?
def f(lst):
    x_y = {}
    for i in range(len(lst) - 1):
        x_y[lst[i+1]] = len(lst[i])
        return x_y
print(f(['17','113']))

#what's the output?
def g(x):
    for i in range(len(x)):
        y = x[i] + x[i]
    return x[i]
print(g([5,7,11]))


# what's the output?
def get_f(n):
    x = 1
    y = 1
    while x <= n:
        y *= x
        y += 1
        return x
print(get_f(2),get_f(3))

def fx(x):
    y = []
    for i in range(len(x)):
        y.append(len(x[i])-i)
    return y

print(fx(['these','are','strings']))

