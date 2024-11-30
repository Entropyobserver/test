def f4(lst):
    new_lst = []
    for word in lst:
        #if word.lower() == "o":
        new_word = word.replace("o","ö")
        new_lst.append(new_word)
    return new_lst
print(f4("Vi  bor  i  Sverige  och  det  kan  kännas  ovant  och  otrevligt  ibland".split()))
