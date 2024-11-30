"""
# 初始列表
my_list = ['apple', 'banana', 'cherry']
print("1. 初始列表:", my_list)
print("\n" + "="*50 + "\n")

# 列表 -> 字符串
print("2. 列表转换为其他数据结构：")
my_str = ', '.join(my_list)
print("列表转字符串:", my_str)

# 列表 -> 元组
my_tuple = tuple(my_list)
print("列表转元组:", my_tuple)

# 列表 -> 集合
my_set = set(my_list)
print("列表转集合:", my_set)

# 列表 -> 字典
my_dict = {i: item for i, item in enumerate(my_list)}
print("列表转字典:", my_dict)
print("\n" + "="*50 + "\n")

# 将这些结构转换回列表
print("3. 其他数据结构转换回列表：")

# 字符串 -> 列表
list_from_str = my_str.split(', ')
print("字符串转回列表:", list_from_str)
print("验证是否与原列表相同:", list_from_str == my_list)

# 元组 -> 列表
list_from_tuple = list(my_tuple)
print("元组转回列表:", list_from_tuple)
print("验证是否与原列表相同:", list_from_tuple == my_list)

# 集合 -> 列表
list_from_set = sorted(list(my_set))  # 使用sorted()确保顺序一致
print("集合转回列表:", list_from_set)
print("验证是否与原列表相同:", list_from_set == my_list)

# 字典 -> 列表
list_from_dict = list(my_dict.values())
print("字典转回列表:", list_from_dict)
print("验证是否与原列表相同:", list_from_dict == my_list)
print("\n" + "="*50 + "\n")

# 数据类型展示
print("4. 各数据结构的类型：")
print(f"原始列表类型: {type(my_list)}")
print(f"字符串类型: {type(my_str)}")
print(f"元组类型: {type(my_tuple)}")
print(f"集合类型: {type(my_set)}")
print(f"字典类型: {type(my_dict)}")
"""

# 初始列表
my_list = ['apple', 'banana', 'cherry']
print("1. 初始列表:", my_list)
print("\n" + "="*50 + "\n")

print("2. 列表转换为其他数据结构：")
print("\n--- 列表转字符串的多种方法 ---")
# 方法1：使用join()方法
str_method1 = ', '.join(my_list)
print("方法1 - join():", str_method1)

# 方法2：使用str()函数
str_method2 = str(my_list)
print("方法2 - str():", str_method2)

## 方法3：使用格式化字符串
#str_method3 = f"{', '.join(my_list)}"
#print("方法3 - f-string:", str_method3)

## 方法4：使用reduce和运算符
#from functools import reduce
#str_method4 = reduce(lambda x, y: str(x) + ', ' + str(y), my_list)
#print("方法4 - reduce:", str_method4)

print("\n--- 列表转元组的多种方法 ---")
# 方法1：使用tuple()函数
tuple_method1 = tuple(my_list)
print("方法1 - tuple():", tuple_method1)

# 方法2：使用*运算符解包
tuple_method2 = (*my_list,)
print("方法2 - 解包运算符:", tuple_method2)

print("\n--- 列表转集合的多种方法 ---")
# 方法1：使用set()函数
set_method1 = set(my_list)
print("方法1 - set():", set_method1)

# 方法2：使用集合推导式
set_method2 = {x for x in my_list}
print("方法2 - 集合推导式:", set_method2)

# 方法3：使用frozenset()（不可变集合）
set_method3 = frozenset(my_list)
print("方法3 - frozenset():", set_method3)

print("\n--- 列表转字典的多种方法 ---")
# 方法1：使用enumerate
dict_method1 = {i: item for i, item in enumerate(my_list)}
print("方法1 - enumerate + 字典推导式:", dict_method1)

# 方法2：使用zip和range
dict_method2 = dict(zip(range(len(my_list)), my_list))
print("方法2 - zip + range:", dict_method2)

# 方法3：创建值为自定义数据的字典
dict_method3 = {item: len(item) for item in my_list}
print("方法3 - 自定义值的字典推导式:", dict_method3)

print("\n" + "="*50 + "\n")

print("3. 其他数据结构转换回列表：")
print("\n--- 字符串转回列表的多种方法 ---")
# 方法1：使用split()
list_from_str1 = str_method1.split(', ')
print("方法1 - split():", list_from_str1)

# 方法2：使用eval()（注意：仅适用于字符串表示的列表）
try:
    list_from_str2 = eval(str_method2)
    print("方法2 - eval():", list_from_str2)
except:
    print("方法2 - eval(): 不适用于当前格式")

# 方法3：使用正则表达式
import re
list_from_str3 = re.findall(r'[^,\s]+', str_method1)
print("方法3 - 正则表达式:", list_from_str3)

print("\n--- 元组转回列表的多种方法 ---")
# 方法1：使用list()函数
list_from_tuple1 = list(tuple_method1)
print("方法1 - list():", list_from_tuple1)

# 方法2：使用列表推导式
list_from_tuple2 = [x for x in tuple_method1]
print("方法2 - 列表推导式:", list_from_tuple2)

# 方法3：使用extend()方法
list_from_tuple3 = []
list_from_tuple3.extend(tuple_method1)
print("方法3 - extend():", list_from_tuple3)

print("\n--- 集合转回列表的多种方法 ---")
# 方法1：使用list()函数
list_from_set1 = sorted(list(set_method1))
print("方法1 - list():", list_from_set1)

# 方法2：使用列表推导式
list_from_set2 = sorted([x for x in set_method1])
print("方法2 - 列表推导式:", list_from_set2)

print("\n--- 字典转回列表的多种方法 ---")
# 方法1：提取值
list_from_dict1 = list(dict_method1.values())
print("方法1 - values():", list_from_dict1)

# 方法2：使用列表推导式获取值
list_from_dict2 = [dict_method1[k] for k in sorted(dict_method1.keys())]
print("方法2 - 列表推导式:", list_from_dict2)

# 方法3：同时获取键和值
list_from_dict3 = [(k, v) for k, v in sorted(dict_method1.items())]
print("方法3 - 键值对列表:", list_from_dict3)

print("\n" + "="*50 + "\n")

print("4. 各数据结构的特点：")
print(f"列表 (list)     : 可变序列，支持索引和切片")
print(f"字符串 (str)    : 不可变序列，支持多种字符串操作")
print(f"元组 (tuple)    : 不可变序列，比列表更节省内存")
print(f"集合 (set)      : 可变无序集合，元素唯一")
print(f"冻结集合 (frozenset): 不可变无序集合，元素唯一")
print(f"字典 (dict)     : 可变映射类型，键值对存储")

print("\n5. 注意事项：")
print("- 字符串转列表时需要考虑分隔符")
print("- 集合会自动去重，转换回列表可能丢失重复元素")
print("- 字典转换需要考虑键值对的处理方式")
print("- eval()方法虽然便捷但有安全风险")
print("- 某些转换可能会改变元素顺序，需要考虑是否需要排序")