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

def main():
    test = [3,5,46,23,5,6,634,6,34,6,7]
    test2 = test.copy()
    test2.sort()
    test3 = sorted(test2)
    print(binary_search_i(test2,6))
    print(binary_search_i(test3,6))
    
main()
