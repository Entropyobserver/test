def f5 (var1, var2) :
    new_lst = []
    for i in range(0, len (var2), 2):
        if var1[i] > i:
            new_lst.append (var1[i])
        else:
            new_lst. append (i)
    return new_lst
a = [1,4,6,2,3,2]
b = [0,2,1,1,5]
print (f5 (a,b))
