def f3():
    new_set1 = set()
    #for i in range(1,1000):
    for i in range(1000):
        if  i % 7 == 0:
            new_set1.add(i)
    return new_set1
print(len(f3()))
def f3():
    new_set2 = set()
    for i in range(1,1000,7):
        new_set2.add(i)
    return new_set2 
print(len(f3()))
def f3():
    new_set3 = set()
    i = 0
    while i < 1000:
        new_set3.add(i)
        i += 7
    return new_set3
print(len(f3()))
