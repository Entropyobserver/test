def bubble_sort(lst):
    if len(lst) <= 1:
        return lst 
    swapped = False
    for i in range(len(lst) - 1):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
            swapped = True
    if not swapped:
        return lst
    return bubble_sort(lst)
if __name__ == "__main__":
    lst = [2, 52, 7, 1, 5]
    print(bubble_sort(lst))