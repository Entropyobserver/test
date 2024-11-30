def bubble_sort(lst):
    """
    Write a function bubble_sort() in bubble_sort_recursive.py that takes a list of
    random integers and returns a list of those numbers sorted
    """

    # if list has 1 or fewer elements, it's already sorted
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
    lst = [5, 1, 4, 2, 8]
    print(bubble_sort(lst))