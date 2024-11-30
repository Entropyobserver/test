from collections import defaultdict

# Initialize sample data
my_dict = {"apple": 5, "banana": 3, "cherry": 7}
fruits = ["apple", "banana", "cherry", "apple", "cherry", "cherry"]
people = {
    "Alice": {"age": 25, "city": "New York"},
    "Bob": {"age": 30, "city": "Chicago"},
    "Charlie": {"age": 35, "city": "San Francisco"}
}
class_subjects = {
    "Alice": ["Math", "Science"],
    "Bob": ["English", "History"],
    "Charlie": ["Art", "PE"]
}

print("Initial data types:")
print(f"my_dict type: {type(my_dict)}")
print(f"my_dict.keys() returns type: {type(my_dict.keys())}")
print(f"my_dict.values() returns type: {type(my_dict.values())}")
print(f"my_dict.items() returns type: {type(my_dict.items())}")
print(f"fruits list type: {type(fruits)}")
print(f"people dict type: {type(people)}")
print(f"class_subjects dict type: {type(class_subjects)}")
print("\n" + "="*50 + "\n")

# 1. Iterate through dictionary keys
print("1. Dictionary keys operation:")
keys = my_dict.keys()
print(f"my_dict.keys() returns type: {type(keys)}")
for key in my_dict:
    print(f"Key: {key}")
print("\n" + "-"*30 + "\n")

# 2. Iterate through dictionary values
print("2. Dictionary values operation:")
values = my_dict.values()
print(f"my_dict.values() returns type: {type(values)}")
for value in values:
    print(f"Value: {value}")
print("\n" + "-"*30 + "\n")

# 3. Iterate through dictionary key-value pairs
print("3. Dictionary items operation:")
items = my_dict.items()
print(f"my_dict.items() returns type: {type(items)}")
for key, value in items:
    print(f"Key: {key}, Value: {value}")
print("\n" + "-"*30 + "\n")

# 4. Filter dictionary key-value pairs
print("4. Dictionary comprehension operation:")
filtered_dict = {key: value for key, value in my_dict.items() if value > 4}
print(f"Dictionary comprehension returns type: {type(filtered_dict)}")
print(f"Filtered dictionary: {filtered_dict}")
print("\n" + "-"*30 + "\n")

# 5. Convert dictionary keys and values to lists
print("5. Converting views to lists:")
keys_list = list(my_dict.keys())
values_list = list(my_dict.values())
print(f"list(dict.keys()) returns type: {type(keys_list)}")
print(f"list(dict.values()) returns type: {type(values_list)}")
print(f"Keys list: {keys_list}")
print(f"Values list: {values_list}")
print("\n" + "-"*30 + "\n")

# 6. Calculate sum of all values
print("6. Sum operation on values:")
values_view = my_dict.values()
print(f"Values view type: {type(values_view)}")
total = sum(values_view)
print(f"Sum result: {total}")
print("\n" + "-"*30 + "\n")

# 7. Swap dictionary keys and values
print("7. Dictionary comprehension for swapping:")
inverted_dict = {value: key for key, value in my_dict.items()}
print(f"Inverted dictionary type: {type(inverted_dict)}")
print(f"Inverted dictionary: {inverted_dict}")
print("\n" + "-"*30 + "\n")

# 8. Update dictionary values
print("8. Dictionary comprehension for updating:")
updated_dict = {key: value + 2 for key, value in my_dict.items()}
print(f"Updated dictionary type: {type(updated_dict)}")
print(f"Updated dictionary: {updated_dict}")
print("\n" + "-"*30 + "\n")

# 9. Merge two dictionaries
print("9. Dictionary merge operation:")
dict1 = {"apple": 5, "banana": 3}
dict2 = {"cherry": 7, "apple": 10}
merged_dict = {**dict1, **dict2}
print(f"Merged dictionary type: {type(merged_dict)}")
print(f"Merged dictionary: {merged_dict}")
print("\n" + "-"*30 + "\n")

# 10. Count occurrences using defaultdict
print("10. defaultdict operation:")
count_dict = defaultdict(int)
print(f"defaultdict type: {type(count_dict)}")
for fruit in fruits:
    count_dict[fruit] += 1
print(f"defaultdict after counting: {dict(count_dict)}")
print(f"Converting to regular dict type: {type(dict(count_dict))}")
print("\n" + "-"*30 + "\n")

# 11. Iterate through nested dictionaries
print("11. Nested dictionary views:")
people_keys = people.keys()
people_values = people.values()
print(f"Nested dict keys type: {type(people_keys)}")
print(f"Nested dict values type: {type(people_values)}")
for person, info in people.items():
    print(f"Person: {person}, Info: {info}")
print("\n" + "-"*30 + "\n")

# 12. Dictionary comprehension with discount
print("12. Dictionary comprehension with calculation:")
discounted_prices = {k: v * 0.9 for k, v in my_dict.items()}
print(f"Discounted prices dict type: {type(discounted_prices)}")
print(f"Discounted prices: {discounted_prices}")
print("\n" + "-"*30 + "\n")

# 13. Iterate through dictionary with nested lists
print("13. Dictionary with nested lists views:")
subjects_view = class_subjects.values()
print(f"Nested lists view type: {type(subjects_view)}")
for student, subjects in class_subjects.items():
    print(f"Student: {student}, Subjects type: {type(subjects)}")
print("\n" + "-"*30 + "\n")

# 14. Using defaultdict for counting
print("14. defaultdict counting operation:")
words = ["apple", "banana", "apple", "cherry", "banana", "banana"]
count_dict_default = defaultdict(int)
print(f"Empty defaultdict type: {type(count_dict_default)}")
for word in words:
    count_dict_default[word] += 1
print(f"Final defaultdict type: {type(count_dict_default)}")
print(f"Converted to regular dict type: {type(dict(count_dict_default))}")
print(f"Final count: {dict(count_dict_default)}")