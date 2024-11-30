def f11(var1, var2):
    var3 = set()
    for i in range(len(var1)):
        var3.add(var1[i])
    return var3

a = {3, 5, 7, 11}
b = [12, 12, 4, 1, 5, 1, 5, 1, 12, 53, 1, 3, 1]
c = f11(b, a)
print(c - a)
