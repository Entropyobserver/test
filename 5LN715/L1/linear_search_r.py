"""
def linear_search(lst, target):
	for element in lst:
		if element == target:
				return True
	return False

def linear_search(lst, target):
    print("Starting linear search...")
    for i, element in enumerate(lst):
        print(f"Step {i+1}: Checking element {element}")
        if element == target:
            print(f"Found target value {target}!")
            return True
    print(f"Target value {target} not found")
    return False

"""
def linear_search_r(lst, n, target):
    # Print current step information
    print(f"Step {n+1}: Checking index {n}")
    print(f"Currently comparing: {lst[n] if n < len(lst) else 'Out of list range'} with target value {target}")
    
    # Base case 1: Out of list range
    if n >= len(lst):
        print("Reached the end of the list, target value not found")
        return False
    
    # Base case 2: Found the target value
    if lst[n] == target:
        print(f"Found target value {target}!")
        return True
    
    # Recursive case
    print(f"Target value not found, continuing to check the next position...\n")
    return linear_search_r(lst, n+1, target)
"""
# Test code
#numbers = [4, 2, 7, 1, 9]
#target = 7
#print(f"Searching for {target} in the list {numbers}")
#result = linear_search_r(numbers, 0, target)

def linear_search_r(lst,n,target):
    #if n >= len(lst):
    #    return False
    if lst[n] == target:
        return True
    return linear_search_r(lst,n+1,target)
#1.everytime compare target with lst[n]
#use n to control how many times we should call this fuction
# if there is no first if condition check,n < 3 it works well,n > 4 list index out of range 

def linear_search_r(lst,n,target):
    #if n <= len(lst)-1 or lst[n] == target:
    #if n <= len(lst)-1 or lst[n] == target:
    if n >= len(lst):
        return False
    if lst[n] == target:
        return True
    return linear_search_r(lst,n+1,target)
"""
def main():
    numbers = [4,56,23,6,7235,73]
    target = 6
    print(f"Searching for {target} in the list {numbers}")
    #print(linear_search(numbers,target))
    print(linear_search_r(numbers,0,target))

main()