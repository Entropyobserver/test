
"""
person = { "name": "John", "age": 30, "city": "New York"}
name = person["name"] 
age = person["age"]
print(name)
print(age)
info = list(person.items())
print(info)
print(person.items())
"""
# Dictionary Methods Demonstration

# Initial dictionary creation
print("1. Creating a Dictionary:")
# Empty dictionary
empty_dict = {}
print("Empty dictionary:", empty_dict)

# Dictionary with initial key-value pairs
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print("Initial person dictionary:", person)
print()

# 2. Accessing Values
print("2. Accessing Values:")
print("Name:", person["name"])
print("Age:", person["age"])
print()

# 3. Adding or Modifying Values
print("3. Adding/Modifying Values:")
print("Before modification:", person)
# Add a new key
person["country"] = "USA"
# Modify existing key
person["city"] = "Chicago"
print("After modification:", person)
print()

# 4. copy() Method
print("4. Copying Dictionary:")
# Create a shallow copy
new_person = person.copy()
# Alternative copy method
another_person = dict(person)
print("Original dictionary:", person)
print("Shallow copy 1:", new_person)
print("Shallow copy 2:", another_person)
# Modify copy to show independence
new_person["age"] = 35
print("Modified copy:", new_person)
print("Original remains unchanged:", person)
print()

# 5. items() Method
print("5. items() Method:")
# Convert dictionary to list of tuples
person_items = list(person.items())
print("Dictionary items:", person_items)
# Iterate through items
print("Iterating through items:")
for key, value in person.items():
    print(f"{key}: {value}")
print()

# 6. Key Existence Check
print("6. Key Existence Check:")
print("Is 'name' in dictionary?", "name" in person)
print("Is 'email' in dictionary?", "email" in person)
print()

# 7. keys() Method
print("7. keys() Method:")
person_keys = list(person.keys())
print("Dictionary keys:", person_keys)
print()

# 8. values() Method
print("8. values() Method:")
person_values = list(person.values())
print("Dictionary values:", person_values)
print()

# 9. update() Method
print("9. update() Method:")
print("Before update:", person)
# Update with new key-value pairs
person.update({"profession": "Doctor", "age": 31})
print("After update:", person)
print()

# 10. clear() Method (demonstrates reset functionality)
print("10. clear() Method:")
grades = {"Math": 95, "Science": 88, "English": 92}
print("Original grades:", grades)
grades.clear()
print("After clear():", grades)
print()

# 11. del Keyword
print("11. del Keyword:")
# Recreate person dictionary for demonstration
person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "country": "USA"
}
print("Before deletion:", person)
# Remove a specific key-value pair
del person["country"]
print("After deletion:", person)