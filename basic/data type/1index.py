def demonstrate_list_indexing():
    # Create a sample list of fruits
    fruits = ["apple", "banana", "peach", "orange", "peach", "grape"]
    print("Original fruit list:", fruits)
    print("\n" + "="*50 + "\n")

    # Method 1: Using enumerate()
    print("Method 1: Using enumerate()")
    for index, fruit in enumerate(fruits):
        print(f"Index: {index}, Element: {fruit}")  # This loops through the list and prints each fruit with its index.
    print("\n" + "="*50 + "\n")

    # Method 2: Using range() and len()
    print("Method 2: Using range() and len()")
    for i in range(len(fruits)):
        print(f"Index: {i}, Element: {fruits[i]}")  # This does the same thing but uses range() and len() to get the indices.
    print("\n" + "="*50 + "\n")

    # Method 3: Using index() to find a specific element
    print("Method 3: Using index() to find a specific element")
    try:
        peach_index = fruits.index("peach")
        print(f"The index of the first 'peach' is: {peach_index}")  # This finds the index of the first occurrence of 'peach'.

        # Find the element starting from a specific index
        second_peach_index = fruits.index("peach", peach_index + 1)
        print(f"The index of the second 'peach' is: {second_peach_index}")  # This finds the index of the second 'peach'.
    except ValueError as e:
        print(f"Error finding element: {e}")  # This handles the case where 'peach' is not found.
    print("\n" + "="*50 + "\n")

    # Method 4: List comprehension to get all indices of a specific element
    print("Method 4: Get all indices of a specific element")
    target = "peach"
    all_indices = [i for i, x in enumerate(fruits) if x == target]
    print(f"All indices of '{target}': {all_indices}")  # This finds all indices of 'peach' using list comprehension.

if __name__ == "__main__":
    demonstrate_list_indexing()
