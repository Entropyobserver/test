def linear_search_r(lst, target, n=0):
    print(f"Step {n+1}: Current search position: Index {n}, Value {lst[n] if n < len(lst) else 'Out of range'}")
    
    if n >= len(lst):
        print(f"Step {n+1}: Completed searching the entire list, target value {target} not found")
        return False
    
    if lst[n] == target:
        print(f"Step {n+1}: Found target value {target}! Located at index {n}")
        return True
    
    print(f"Step {n+1}: {lst[n]} != {target}, continuing search")
    return linear_search_r(lst, target, n+1)

if __name__ == "__main__":
    numbers = [4, 56, 23, 6, 7235, 73]
    target = 6
    print("Original list:", numbers)
    print("Search target:", target)
    result = linear_search_r(numbers, target, 0)
    print("Search result:", result)
