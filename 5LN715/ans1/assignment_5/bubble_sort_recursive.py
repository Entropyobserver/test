def bubble_sort(lst):
    """
    Sort a list of integers using the bubble sort algorithm recursively. 
    Parameters: lst (list): The list of integers to be sorted. 
    Returns: list: The sorted list of integers. 
    """

    # Base case: if list has 1 or fewer elements, it's already sorted
    if len(lst) <= 1:
        return lst
    
    # Flag to track if any swaps occurred in this pass
    swapped = False
    
    # Traverse the list, comparing adjacent elements
    for i in range(len(lst) - 1):
        # If adjacent elements are in wrong order, swap them
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
            swapped = True
    
    # If no swaps occurred, the list is already sorted
    if not swapped:
        return lst
    
    # Recursively continue sorting
    return bubble_sort(lst)
if __name__ == "__main__":
    lst = [2, 52, 7, 1, 5]
    print(bubble_sort(lst))