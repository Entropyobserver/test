dict_with_list = {'a': [1, 2, 3], 'b': [4, 5, 6]}
for key, lst in dict_with_list.items():
    for value in lst:
        print(f"{key}: {value}")

# Demonstrate dictionary with lists and nested iteration
# Initial dictionary where each key is associated with a list of values
dict_with_list = {'a': [1, 2, 3], 'b': [4, 5, 6]}

print("Initial Dictionary:")
print("dict_with_list =", dict_with_list)

# Explanation of .items() method
print("\n.items() method converts dictionary to a list of (key, value) tuples:")
print("List of tuples:", list(dict_with_list.items()))

print("\nBeginning nested loop execution:\n")

# Outer loop iterates through dictionary items using .items() method
for key, lst in dict_with_list.items():
    print(f"--- Outer loop starts: Current key = '{key}', Current list = {lst} ---")
    
    # Inner loop iterates through each value in the list associated with the current key
    for value in lst:
        print(f"  Inner loop starts: Current value = {value}")
        print(f"  Generate and print combination: {key}: {value}")
        print(f"{key}: {value}")
        print("  Inner loop continues")
    
    print(f"--- Outer loop with key '{key}' ends ---\n")

print("Program execution completed")