"""

    Assign a list of lists to a variable lst_of_lsts
    Each list in the list of lists should contain 3 integers.
    Let them range from 1 to 9 so that the first list contains 1, 2, and 3
    (the second list 4, 5 and 6, and the third list 7, 8, and 9).

    Print the sum of the sums of all three lists

    Hint: Assign each list in the list to their own variables.

    The output should be

    45

"""
lst_of_lsts = [[1,2,3],[4,5,6],[7,8,9]]
list1 = lst_of_lsts[0]
list2 = lst_of_lsts[1]
list3 = lst_of_lsts[2]
sum = sum(list1) + sum(list2) + sum(list3)
print(sum)
