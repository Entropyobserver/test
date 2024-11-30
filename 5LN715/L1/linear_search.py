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

# Test code
#numbers = [4, 2, 7, 1, 9]
#target = 7
#print(f"Searching for {target} in the list {numbers}")
#result = linear_search(numbers, target)

def main():
    numbers = [4,56,23,6,7235,73]
    target = 6
    print(f"Searching for {target} in the list {numbers}")
    print(linear_search(numbers,target))
    #print(linear_search_r(test,3,6))
main()
