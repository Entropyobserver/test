def column_correct(list : list,column_num : int):
    n_list = []
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][column_num] > 0 and list[i][column_num] in n_list:
                return False
        else:
            n_list.append(list[i][column_num])
    return True