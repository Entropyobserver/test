#find u
lst = ['dog','cat','turtle','lion']
print(lst)
print('turtle'[1])
print(lst[3][2])
print(lst[2][1])

#what is the output？
def f(m):
    n = m + m
    a = n * n
    return a
print(f(4))

def g(m):
    if len(m) > 2:
        if len(m) > 4:
            return m[3]
        else:
            return m[2]
print(g([1,2,3]))

def h(m):
    lst = []
    for i in range(m):
        if i + 1 < 3:
            lst.append(i)
    return lst
print(h(5))
