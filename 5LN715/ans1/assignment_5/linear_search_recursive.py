def linear_search(lst, target, n=0):
"""
Searches for a target value in a list using an recursive linear search.

Parameters:
lst (list): The list of numbers to search through.
target (int): The target value to search for.
n (int): The starting index for the search (default is 0).

Returns:
bool: Whether the target value is found or not.
"""
    for i in range(n, len(lst)):
        if lst[i] == target:# Immediately return True if the target value is found
            return True
    return False# Return False if the target value is not found

if __name__ == "__main__":
    numbers = [29, 87, 89, 21, 23, 17, 11, 10, 14]
    target = 17
    print("Original list:", numbers)
    print("target:", target)
    result = linear_search(numbers, target)
    print("result:", result)
