def bubble_sort_interative(lst):
    n = len(lst)
    # The outer loop should run n-1 times to cover all possible comparisons
    for i in range(n-1):
        # a swap flag to check if any swap has occurred 
        swap = False
        # The inner loop range is correct, reducing the number of sorted elements each time
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                # Mark that a swap has occurred
                swap = True
        # If no swaps occurred in a round, the list is already sorted
        if not swap:
            break
    return lst

if __name__ == "__main__":
    lst = [5, 1, 4, 2, 8]
    print(bubble_sort_interative(lst))