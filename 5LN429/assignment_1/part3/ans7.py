def f7(lst):
    new_lst = []
    for i in range(len(lst)-1):
        #new_lst.append(lst[i:i+1])
        new_lst.append(lst[i:i+2])
    return new_lst
myString = "here is an example sentence"
myList = myString.split()
print(f7(myList))

