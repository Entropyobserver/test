def binary_search_recursive(data, target):
    middle = len(lst) // 2
    if lst[middle] == target:
       return True
    elif  target < lst[middle]:
        return binary_search_recursive(lst[:middle],target)
    else:
        return binary_search_recursive(lst[middle+1:], target)

if __name__ == "__main__":
    lst = [3,5,46,23,5,6,634,6,34,6,7]
    print(binary_search_recursive(lst,6))
