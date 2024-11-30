def f2(lst):
    new_lst = []
    for i in range(len(lst)):
        new_lst.append(lst[i-1]+' '+lst[i])
    return new_lst
print(f2("colorless green ideas sleep furiously".split()))
