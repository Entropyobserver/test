"""

def demonstrate_set_operations():
    print("\n1. 创建集合")
    # 创建一个空集合
    empty_set = set()
    print(f"空集合: {empty_set}")
    
    # 创建两个有初始值的集合
    fruits = {"apple", "banana", "orange"}
    colors = {"red", "blue", "orange", "green"}
    print(f"fruits集合: {fruits}")
    print(f"colors集合: {colors}")

    print("\n2. 添加元素 (add)")
    fruits.add("mango")
    print(f"添加'mango'后的fruits: {fruits}")
    # 尝试添加重复元素
    fruits.add("mango")
    print(f"尝试再次添加'mango'后的fruits(注意不会重复): {fruits}")

    print("\n3. 更新集合 (update)")
    fruits.update(["kiwi", "grape"])
    print(f"使用update添加多个元素后的fruits: {fruits}")

    print("\n4. 复制集合 (copy)")
    new_fruits = fruits.copy()
    print(f"复制的新集合: {new_fruits}")

    print("\n5. 移除元素 (discard)")
    fruits.discard("apple")
    print(f"移除'apple'后的fruits: {fruits}")
    # discard不存在的元素不会报错
    fruits.discard("pineapple")
    print(f"尝试移除不存在的'pineapple'后的fruits: {fruits}")

    print("\n6. 弹出元素 (pop)")
    popped_item = fruits.pop()
    print(f"弹出的元素: {popped_item}")
    print(f"弹出元素后的fruits: {fruits}")

    print("\n7. 移除指定元素 (remove)")
    fruits.remove("banana")
    print(f"移除'banana'后的fruits: {fruits}")
    # 如果尝试移除不存在的元素会抛出错误
    # fruits.remove("pineapple")  # 这会引发KeyError

    print("\n8. 检查超集关系 (issuperset)")
    set1 = {"apple", "banana"}
    set2 = {"apple"}
    is_superset = set1.issuperset(set2)
    print(f"set1: {set1}")
    print(f"set2: {set2}")
    print(f"set1是set2的超集吗？ {is_superset}")

    print("\n9. 检查子集关系 (issubset)")
    is_subset = set2.issubset(set1)
    print(f"set2是set1的子集吗？ {is_subset}")

    print("\n10. 集合操作")
    print("原始集合:")
    print(f"fruits: {fruits}")
    print(f"colors: {colors}")
    
    # 并集
    union_set = fruits.union(colors)
    print(f"并集: {union_set}")
    
    # 交集
    intersection_set = fruits.intersection(colors)
    print(f"交集: {intersection_set}")
    
    # 差集
    difference_set = fruits.difference(colors)
    print(f"差集 (fruits - colors): {difference_set}")
    
    # 对称差集
    symmetric_difference = fruits.symmetric_difference(colors)
    print(f"对称差集: {symmetric_difference}")

    print("\n11. 清空集合 (clear)")
    new_fruits.clear()
    print(f"清空后的new_fruits: {new_fruits}")

# 执行演示
demonstrate_set_operations()



"""
def demonstrate_set_operations():
   print("\n1. Creating Sets")
   print("Method used: set()")
   empty_set = set()
   print(f"Empty set: {empty_set}")
   
   fruits = {"apple", "banana", "orange"}
   colors = {"red", "blue", "orange", "green"}
   print(f"fruits set: {fruits}")
   print(f"colors set: {colors}")

   print("\n2. Adding Elements")
   print("Method used: add() ")
   fruits.add("mango")
   print(f"fruits after adding 'mango': {fruits}")
   fruits.add("mango")
   print(f"fruits after trying to add 'mango' again (note: no duplicates): {fruits}")

   print("\n3. Updating Set")
   print("Method used: update()")
   fruits.update(["kiwi", "grape"])
   print(f"fruits after updating with multiple elements: {fruits}")

   print("\n4. Copying Set")
   print("Method used: copy()")
   new_fruits = fruits.copy()
   print(f"New copied set: {new_fruits}")

   print("\n5. Removing Elements using discard")
   print("Method used: discard()")
   fruits.discard("apple")
   print(f"fruits after discarding 'apple': {fruits}")
   fruits.discard("pineapple")
   print(f"fruits after trying to discard non-existent 'pineapple': {fruits}")

   print("\n6. Popping Elements")
   print("Method used: pop()")
   popped_item = fruits.pop()
   print(f"Popped item: {popped_item}")
   print(f"fruits after popping: {fruits}")

   print("\n7. Removing Specific Element")
   print("Method used: remove()")
   fruits.remove("banana")
   print(f"fruits after removing 'banana': {fruits}")

   print("\n8. Checking Superset Relationship")
   print("Method used: issuperset()")
   set1 = {"apple", "banana"}
   set2 = {"apple"}
   is_superset = set1.issuperset(set2)
   print(f"set1: {set1}")
   print(f"set2: {set2}")
   print(f"Is set1 a superset of set2? {is_superset}")

   print("\n9. Checking Subset Relationship")
   print("Method used: issubset()")
   is_subset = set2.issubset(set1)
   print(f"Is set2 a subset of set1? {is_subset}")

   print("\n10. Set Operations")
   print("Original sets:")
   print(f"fruits: {fruits}")
   print(f"colors: {colors}")

   print("\nUnion")
   print("Method used: union()")
   union_set = fruits.union(colors)
   print(f"Union: {union_set}")

   print("\nIntersection")
   print("Method used: intersection()")
   intersection_set = fruits.intersection(colors)
   print(f"Intersection: {intersection_set}")

   print("\nDifference")
   print("Method used: difference()")
   difference_set = fruits.difference(colors)
   print(f"Difference (fruits - colors): {difference_set}")

   print("\nSymmetric Difference")
   print("Method used: symmetric_difference()")
   symmetric_difference = fruits.symmetric_difference(colors)
   print(f"Symmetric difference: {symmetric_difference}")

   print("\n11. Clearing Set")
   print("Method used: clear()")
   new_fruits.clear()
   print(f"new_fruits after clearing: {new_fruits}")

print("Executing Set Operations Demonstration:")
demonstrate_set_operations()