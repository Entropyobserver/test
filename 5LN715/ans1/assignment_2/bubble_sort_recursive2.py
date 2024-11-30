def bubble_sort(lst, n):
    print(f"Current list: {lst}, n = {n}")  # Add print statement
    
    if n <= 1:
        return lst
    
    for i in range(n-1):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
            print(f"Swapping {lst[i]} and {lst[i+1]}: {lst}")  # Print swap process
    
    return bubble_sort(lst, n-1)

if __name__ == "__main__":
    lst = [2, 52, 7, 1, 5, 6, 35, 23, 789, 86, 24, 90, 346, 236, 123, 54, 21]
    n = len(lst)
    print("Original list:", lst)
    result = bubble_sort(lst, n)
    print("Final sorted result:", result)
