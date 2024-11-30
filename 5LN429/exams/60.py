def f10a(_):
    if _ % 3 == 0:
        return True
    return False

def f10b(_):
    if _ % 2 == 0:
        return False
    return True

def g10(lst):
    lst_ = [f10a(x) for x in lst]
    _lst = [x for x in lst if f10b(x)]
    return _lst,lst_

def main():
    a = [2, 3, 4, 12, 15, 21, 40]
    print(sum(g10(a)[0]))
    print(g10(a)[1])

main()
