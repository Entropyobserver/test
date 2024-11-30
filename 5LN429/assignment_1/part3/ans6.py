def f6(lst):
    new_lst = []
    #for i in lst:
    for i in range(len(lst)):
        new_lst.append(lst[:i+1])
    return new_lst
words = "these are some words that we use" 
print(f6(words.split()))
