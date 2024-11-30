import copy  # Import the copy module for deep copying

# 1. Demonstrating Shallow Copy
print("\n--- Shallow Copy Demo ---")
# Create an original list with nested lists
original_list = [1, [2, 3], ['a', 'b']]
print("Original list:", original_list)
# Perform a shallow copy using the copy() method
shallow_copy = original_list.copy()
print("Shallow copy:", shallow_copy)
# Modify the nested list in the original list
original_list[1][0] = 'X'
print("\nAfter modifying nested list in original:")
print("Original list:", original_list)
print("Shallow copy:", shallow_copy)  # The nested list is also modified because only the reference is copied
# Modify the top-level element in the original list
original_list[0] = 'Y'
print("\nAfter modifying top-level element in original:")
print("Original list:", original_list)
print("Shallow copy:", shallow_copy)  # The top-level element is not affected because it is an independent copy

# 2. Demonstrating Deep Copy
print("\n--- Deep Copy Demo ---")
# Create a new original list
original_list = [1, [2, 3], ['a', 'b']]
print("Original list:", original_list)
# Perform a deep copy using copy.deepcopy()
deep_copy = copy.deepcopy(original_list)
print("Deep copy:", deep_copy)
# Modify the nested list in the original list
original_list[1][0] = 'X'
print("\nAfter modifying nested list in original:")
print("Original list:", original_list)
print("Deep copy:", deep_copy)  # The nested list is not affected because it is a completely independent copy
# Modify the top-level element in the original list
original_list[0] = 'Y'
print("\nAfter modifying top-level element in original:")
print("Original list:", original_list)
print("Deep copy:", deep_copy)  # The top-level element is also not affected

# 3. Comparison of Different Copy Methods
print("\n--- Comparison of Different Copy Methods ---")
original = [1, [2, 3], ['a', 'b']]
reference = original  # Reference assignment
shallow = original.copy()  # Shallow copy
deep = copy.deepcopy(original)  # Deep copy
print("Initial state:")
print("Original:", original)
print("Reference:", reference)
print("Shallow copy:", shallow)
print("Deep copy:", deep)
# Modify the nested list
original[1][0] = 'X'
print("\nAfter modifying nested list:")
print("Original:", original)
print("Reference:", reference)  # Changed
print("Shallow copy:", shallow)  # Changed
print("Deep copy:", deep)  # Not changed
"""
这个代码展示了三种不同的复制方式的区别：

引用赋值 (Reference Assignment):

直接使用 = 赋值
创建一个新的引用指向同一个对象
原始列表的任何改变都会影响到引用


浅拷贝 (Shallow Copy):

使用 copy() 方法或 list() 构造函数
创建一个新列表，但只复制顶层元素的引用
对于嵌套的可变对象（如列表），仍然共享同一个引用
修改原始列表的顶层元素不会影响浅拷贝
修改嵌套的可变对象会影响浅拷贝


深拷贝 (Deep Copy):

使用 copy.deepcopy()
创建一个全新的独立副本
递归地复制所有嵌套的对象
原始列表的任何修改都不会影响深拷贝
完全独立的两个对象



使用场景：

如果列表只包含不可变对象（数字、字符串、元组），用浅拷贝就足够了
如果列表包含嵌套的可变对象（列表、字典），而且需要完全独立的副本，应该使用深拷贝
如果只需要创建另一个引用指向同一个对象，使用简单的赋值

注意事项：

深拷贝比浅拷贝消耗更多内存和计算资源
对于复杂的数据结构，深拷贝可能会导致无限递归
在处理大型数据结构时要谨慎使用深拷贝
"""
