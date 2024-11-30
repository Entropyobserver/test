
def f2():
    new_tu = set()
    for i in range(1,100001):
        if i % 13 == 0:
            new_tu.add(i)
    return (len(new_tu),sum(new_tu))
print(f2())

def f2():
    count = 0
    total = 0
    for i in range(1,100001):
        if i % 13 == 0:
            count += 1
            total += i
    return count,total
print(f2())

