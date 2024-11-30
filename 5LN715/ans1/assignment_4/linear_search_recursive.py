def linear_search(lst, target, n=0):
    """
    Searches for a target value in a list using a recursive linear search.

    Parameters:
    lst (list): The list of numbers to search through.
    target (int): The target value to search for.
    n (int): The starting index for the search (default is 0).

    Returns:
    bool: Whether the target value is found or not.
    """
    if n >= len(lst):
        return False
    if lst[n] == target:
        return True
    return linear_search(lst, target, n + 1)

if __name__ == "__main__":
    numbers = [29, 87, 89, 21, 23, 17, 11, 10, 14]
    target = 17
    print("Original list:", numbers)
    print("Target:", target)
    result = linear_search(numbers, target)
    print("Result:", result)

