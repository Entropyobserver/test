def binary_search_recursive(lst, target):
    if not lst:
        return False
    middle = len(lst) // 2
    if lst[middle] == target:
       return True
    elif  target < lst[middle]:
        return binary_search_recursive(lst[:middle],target)
    else:
        return binary_search_recursive(lst[middle+1:], target)
if __name__ == "__main__":
    lst = [1, 3, 5, 7, 9, 11, 13, 15, 17]
    print(binary_search_recursive(lst,6))
