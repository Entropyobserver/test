def f3(lst):
    new_lst = []
    for i in lst:
        #if i % 2 == 0 and isinstance(i,int):
        #if isinstance(i,int) and i % 2 == 0:
        if type(i) == int and i % 2 == 0:
            new_lst.append(i)
    return new_lst
print(f3(['words', 6598, 'I', 6336, 'put', 7545, 'I', 8839, 'that', 5379, 'together', 1114,
         'that', 6204, 'together', 6070, 'words', 8564, 'are', 8036]))
