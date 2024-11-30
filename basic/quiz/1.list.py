lst1 = [1,2,3,4]
lst2 = lst1[:-1]
lst1.append(1)
print(lst2)
#The key point here is that lst2 was created as a slice of lst1 before lst1 was modified. 
# Therefore, lst2 remains unaffected by the changes made to lst1 after the slice was taken.