def gen1():
    for i in range(3):
        yield i

def gen2():
    for j in range(2):
        yield j

for i in gen1():
    for j in gen2():
        print(i, j)