def f11(s):
    x = s. split ()[:8]
    z = []
    for y in x:
        z.append(len(y))
    return z

def g11(a) :
    b = []
    for c in a:
        if c > 3:
            b.append(str(c).split(".")[0])
    return b

h = "It is often safer to be in chains than to be free."
t = f11(h)
k = set(g11(t))
print(k)

#y = []
#y.append(str(5).split(".")[0])
#print(y)
#The split(".") method in Python is used to split a string into a list of substrings based on the delimiter provided, which in this case is the period (".")