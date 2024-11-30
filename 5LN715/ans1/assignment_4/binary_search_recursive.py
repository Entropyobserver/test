def binary_search(lst, target):
    """
    Search for a target value in a sorted list using a recursive binary search.

    Parameters:
    lst (list): The sorted list of numbers to search through.
    target (int): The target value to search for.

    Returns:
    bool: True if the target value is found, otherwise False.
    """
    # If the list is empty, return False
    if len(lst) == 0:
        return False
    
    mid = len(lst) // 2
    
    if lst[mid] == target:
        return True
    elif target < lst[mid]:
        # Recursively search the left half of the list
        return binary_search(lst[:mid], target)
    else:
        # Recursively search the right half of the list
        return binary_search(lst[mid+1:], target)

if __name__ == "__main__":
    lst = [29, 87, 89, 21, 23, 17, 11, 10, 14]
    sorted_numbers = sorted(lst)
    target = 17
    print("Sorted list:", sorted_numbers)
    print("target:", target)
    result = binary_search(sorted_numbers, target)
    print("result:", result)

