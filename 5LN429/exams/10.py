def f10(varl,var2) :
    for n in varl:
        var2.add(n)
    return var2

d = {1,2,3,4}
test = f10 ( [1,2,4,5,99], d)
print (len(test), type(test))