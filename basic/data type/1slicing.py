lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Print the entire list:")
print(lst[:])  # This prints the whole list as it is. Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("\nReverse the list:")
print(lst[::-1])  # This reverses the list. Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print("\nPrint from the 4th element to the end:")
print(lst[3:])  # This prints the list starting from the 4th element to the end. Output: [4, 5, 6, 7, 8, 9, 10]

print("\nPrint the last 3 elements:")
print(lst[-3:])  # This prints the last 3 elements of the list. Output: [8, 9, 10]

print("\nPrint the first 7 elements:")
print(lst[:-3])  # This prints the first 7 elements of the list. Output: [1, 2, 3, 4, 5, 6, 7]

print("\nPrint elements at odd indices:")
print(lst[::2])  # This prints elements at odd indices (1st, 3rd, 5th, etc.). Output: [1, 3, 5, 7, 9]

print("\nPrint elements at even indices:")
print(lst[1::2])  # This prints elements at even indices (2nd, 4th, 6th, etc.). Output: [2, 4, 6, 8, 10]

print("\nPrint the 3rd to the 2nd last element:")
print(lst[-3:-1])  # This prints elements from the 3rd last to the 2nd last. Output: [8, 9]

print("\nPrint elements from index 2 to 5 (excluding 6):")
print(lst[2:6])  # This prints elements from index 2 to 5 (6 is excluded). Output: [3, 4, 5, 6]

# Additional challenging examples:
print("\nPrint every 3rd element:")
print(lst[::3])  # This prints every 3rd element in the list. Output: [1, 4, 7, 10]

print("\nPrint elements from index 1 to 8 with a step of 2:")
print(lst[1:9:2])  # This prints elements from index 1 to 8, taking every 2nd element. Output: [2, 4, 6, 8]
