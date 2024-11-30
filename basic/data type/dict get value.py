"""
print("\n1. 使用键直接访问：")
my_dict = {"a": 1, "b": 2}
print(f"初始字典: {my_dict}")
print("尝试访问键'a'")
value = my_dict["a"]
print(f"获取到的值: value = {value}")

print("\n2. 使用get()方法：")
my_dict = {"a": 1, "b": 2}
print(f"初始字典: {my_dict}")
print("尝试使用get()访问键'a'")
value = my_dict.get("a", 0)
print(f"获取到的值: value = {value}")
print("尝试使用get()访问不存在的键'c'")
value = my_dict.get("c", 0)
print(f"获取到的值: value = {value} (使用默认值0)")

print("\n3. 使用setdefault()方法：")
my_dict = {"a": 1, "b": 2}
print(f"初始字典: {my_dict}")
print("使用setdefault()设置键'c'的默认值为3")
value = my_dict.setdefault("c", 3)
print(f"获取到的值: value = {value}")
print(f"更新后的字典: {my_dict}")

print("\n4. 使用keys()方法：")
my_dict = {"a": 1, "b": 2}
print(f"初始字典: {my_dict}")
print("获取所有键")
keys = my_dict.keys()
print(f"字典的键: {keys}")

print("\n5. 使用values()方法：")
my_dict = {"a": 1, "b": 2}
print(f"初始字典: {my_dict}")
print("获取所有值")
values = my_dict.values()
print(f"字典的值: {values}")

print("\n6. 使用items()方法：")
my_dict = {"a": 1, "b": 2}
print(f"初始字典: {my_dict}")
print("获取所有键值对")
items = my_dict.items()
print(f"字典的键值对: {items}")

print("\n7. 使用pop()方法：")
my_dict = {"a": 1, "b": 2}
print(f"初始字典: {my_dict}")
print("尝试弹出键'a'")
value = my_dict.pop("a", 0)
print(f"弹出的值: value = {value}")
print(f"弹出后的字典: {my_dict}")

print("\n8. 使用popitem()方法：")
my_dict = {"a": 1, "b": 2}
print(f"初始字典: {my_dict}")
print("使用popitem()弹出最后一个键值对")
key, value = my_dict.popitem()
print(f"弹出的键值对: key = {key}, value = {value}")
print(f"弹出后的字典: {my_dict}")

print("\n1. Accessing using key directly:")
my_dict = {"a": 1, "b": 2}
print(f"Initial dictionary: {my_dict}")
print("Trying to access key 'a'")
value = my_dict["a"]
print(f"Retrieved value: value = {value}")

print("\n2. Using get() method:")
my_dict = {"a": 1, "b": 2}
print(f"Initial dictionary: {my_dict}")
print("Trying to access key 'a' using get()")
value = my_dict.get("a", 0)
print(f"Retrieved value: value = {value}")
print("Trying to access non-existent key 'c' using get()")
value = my_dict.get("c", 0)
print(f"Retrieved value: value = {value} (using default value 0)")

print("\n3. Using setdefault() method:")
my_dict = {"a": 1, "b": 2}
print(f"Initial dictionary: {my_dict}")
print("Using setdefault() to set default value for key 'c' to 3")
value = my_dict.setdefault("c", 3)
print(f"Retrieved value: value = {value}")
print(f"Updated dictionary: {my_dict}")

print("\n4. Using keys() method:")
my_dict = {"a": 1, "b": 2}
print(f"Initial dictionary: {my_dict}")
print("Getting all keys")
keys = my_dict.keys()
print(f"Keys in the dictionary: {keys}")

print("\n5. Using values() method:")
my_dict = {"a": 1, "b": 2}
print(f"Initial dictionary: {my_dict}")
print("Getting all values")
values = my_dict.values()
print(f"Values in the dictionary: {values}")

print("\n6. Using items() method:")
my_dict = {"a": 1, "b": 2}
print(f"Initial dictionary: {my_dict}")
print("Getting all key-value pairs")
items = my_dict.items()
print(f"Key-value pairs in the dictionary: {items}")

print("\n7. Using pop() method:")
my_dict = {"a": 1, "b": 2}
print(f"Initial dictionary: {my_dict}")
print("Trying to pop key 'a'")
value = my_dict.pop("a", 0)
print(f"Popped value: value = {value}")
print(f"Dictionary after pop: {my_dict}")

print("\n8. Using popitem() method:")
my_dict = {"a": 1, "b": 2}
print(f"Initial dictionary: {my_dict}")
print("Using popitem() to pop the last key-value pair")
key, value = my_dict.popitem()
print(f"Popped key-value pair: key = {key}, value = {value}")
print(f"Dictionary after popitem: {my_dict}")



print("\n1. Accessing using key directly:")
my_dict = {"a": 1, "b": 2}
print(f"Initial dictionary: {my_dict}")  # Type: dict
print("Trying to access key 'a'")
value = my_dict["a"]
print(f"Retrieved value: value = {value}")  # Type: int (depends on the value stored)

print("\n2. Using get() method:")
my_dict = {"a": 1, "b": 2}
print(f"Initial dictionary: {my_dict}")  # Type: dict
value = my_dict.get("a", 0)
print(f"Return type of get(): {type(value)}")  # Type: int (depends on the value stored or default value)

print("\n3. Using setdefault() method:")
my_dict = {"a": 1, "b": 2}
value = my_dict.setdefault("c", 3)
print(f"Return type of setdefault(): {type(value)}")  # Type: int (depends on the value set)

print("\n4. Using keys() method:")
my_dict = {"a": 1, "b": 2}
keys = my_dict.keys()
print(f"Return type of keys(): {type(keys)}")  # Type: dict_keys (view object)

print("\n5. Using values() method:")
my_dict = {"a": 1, "b": 2}
values = my_dict.values()
print(f"Return type of values(): {type(values)}")  # Type: dict_values (view object)

print("\n6. Using items() method:")
my_dict = {"a": 1, "b": 2}
items = my_dict.items()
print(f"Return type of items(): {type(items)}")  # Type: dict_items (view object)

print("\n7. Using pop() method:")
my_dict = {"a": 1, "b": 2}
value = my_dict.pop("a", 0)
print(f"Return type of pop(): {type(value)}")  # Type: int (depends on the value popped)

print("\n8. Using popitem() method:")
my_dict = {"a": 1, "b": 2}
key, value = my_dict.popitem()
print(f"Return type of popitem(): {type((key, value))}")  # Type: tuple containing (str, int)
"""
print("\n1. Accessing using key directly:")
my_dict = {"a": 1, "b": 2}
print(f"Initial dictionary: {my_dict}")
print("Trying to access key 'a'")
value = my_dict["a"]
print(f"Retrieved value: value = {value}")
print(f"Return type of direct access: {type(value)}")  # Type: int (depends on stored value)

print("\n2. Using get() method:")
my_dict = {"a": 1, "b": 2}
print(f"Initial dictionary: {my_dict}")
print("Trying to access key 'a' using get()")
value = my_dict.get("a", 0)
print(f"Retrieved value: value = {value}")
print(f"Return type of get(): {type(value)}")  # Type: int (depends on value/default)
print("Trying to access non-existent key 'c' using get()")
value = my_dict.get("c", 0)
print(f"Retrieved value: value = {value} (using default value 0)")
print(f"Return type of get() with default: {type(value)}")

print("\n3. Using setdefault() method:")
my_dict = {"a": 1, "b": 2}
print(f"Initial dictionary: {my_dict}")
print("Using setdefault() to set default value for key 'c' to 3")
value = my_dict.setdefault("c", 3)
print(f"Retrieved value: value = {value}")
print(f"Updated dictionary: {my_dict}")
print(f"Return type of setdefault(): {type(value)}")  # Type: int (depends on set value)

print("\n4. Using keys() method:")
my_dict = {"a": 1, "b": 2}
print(f"Initial dictionary: {my_dict}")
print("Getting all keys")
keys = my_dict.keys()
print(f"Keys in the dictionary: {keys}")
print(f"Return type of keys(): {type(keys)}")  # Type: dict_keys (view object)

print("\n5. Using values() method:")
my_dict = {"a": 1, "b": 2}
print(f"Initial dictionary: {my_dict}")
print("Getting all values")
values = my_dict.values()
print(f"Values in the dictionary: {values}")
print(f"Return type of values(): {type(values)}")  # Type: dict_values (view object)

print("\n6. Using items() method:")
my_dict = {"a": 1, "b": 2}
print(f"Initial dictionary: {my_dict}")
print("Getting all key-value pairs")
items = my_dict.items()
print(f"Key-value pairs in the dictionary: {items}")
print(f"Return type of items(): {type(items)}")  # Type: dict_items (view object)

print("\n7. Using pop() method:")
my_dict = {"a": 1, "b": 2}
print(f"Initial dictionary: {my_dict}")
print("Trying to pop key 'a'")
value = my_dict.pop("a", 0)
print(f"Popped value: value = {value}")
print(f"Dictionary after pop: {my_dict}")
print(f"Return type of pop(): {type(value)}")  # Type: int (depends on popped value)

print("\n8. Using popitem() method:")
my_dict = {"a": 1, "b": 2}
print(f"Initial dictionary: {my_dict}")
print("Using popitem() to pop the last key-value pair")
key, value = my_dict.popitem()
print(f"Popped key-value pair: key = {key}, value = {value}")
print(f"Dictionary after popitem: {my_dict}")
print(f"Return type of popitem(): {type((key, value))}")  # Type: tuple

print("\nReturn Types Summary:")
print("1. Direct key access: Returns the value type stored (int, str, list, etc.)")
print("2. get(): Returns the value type stored or default value type")
print("3. setdefault(): Returns the value type stored or default value type")
print("4. keys(): Returns dict_keys object (view object)")
print("5. values(): Returns dict_values object (view object)")
print("6. items(): Returns dict_items object (view object)")
print("7. pop(): Returns the value type that was popped")
print("8. popitem(): Returns a tuple containing (key, value)")

print("\nNote:")
print("- View objects (dict_keys, dict_values, dict_items) are dynamic views of dictionary entries")
print("- Actual value types depend on what's stored in the dictionary")
print("- All methods maintain dictionary structure (key-value pairs)")
print("- Default values can be of any type, not just integers as shown in examples")