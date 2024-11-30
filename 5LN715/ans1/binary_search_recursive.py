"""
def binary_search_i(data, value):
    n = len(data)
    left = 0
    right = n - 1
    while left <= right:
        middle = (left + right) // 2
        if value < data[middle]:
            right = middle - 1
        elif value > data[middle]:
            left = middle + 1
        else:
            return middle
    raise ValueError('Value is not in the list')

def binary_search_i(data, value, n):
    n = len(data)
    left = 0
    right = n - 1
    if left <= right:
        middle = (left + right) // 2
        if value < data[middle]:
            right = middle - 1
        elif value > data[middle]:
            left = middle + 1
        else:
            return middle
    raise ValueError('Value is not in the list')
    return binary_search_i(data,value,n-1)
"""
def binary_search_recursive(data, value, left, right):
    if left > right:
       return False
    middle = (left + right) // 2
    if value == data[middle]:
        return True
    elif value < data[middle]:
        return binary_search_recursive(data, value, left, middle - 1)
    else:
        return binary_search_recursive(data, value, middle + 1, right)

def main():
    lst = [3,5,46,23,5,6,634,6,34,6,7]
    left = 0
    right = len(lst) - 1
    print(binary_search_recursive(lst,6,left,right))

main()
