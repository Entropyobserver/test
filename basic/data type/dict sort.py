import operator
from collections import OrderedDict

# 创建示例字典
my_dict = {'b': 3, 'a': 1, 'c': 2, 'd': 4}
print("原始字典:")
print(my_dict)
print("\n" + "="*50 + "\n")

# 1. 按键（Keys）排序
print("1. 按键排序:")
# 展示排序过程
print("1.1 转换为items()列表:")
items_list = list(my_dict.items())
print(items_list)

print("\n1.2 使用sorted()按键排序:")
sorted_by_keys = sorted(my_dict.items())
print(sorted_by_keys)

print("\n1.3 转换回字典:")
dict_sorted_by_keys = dict(sorted_by_keys)
print(dict_sorted_by_keys)
print("\n" + "="*50 + "\n")

# 2. 按值（Values）排序
print("2. 按值排序:")
print("2.1 使用lambda函数方式:")
sorted_by_values_lambda = sorted(my_dict.items(), key=lambda x: x[1])
print(sorted_by_values_lambda)
print("转换为字典:", dict(sorted_by_values_lambda))

print("\n2.2 使用operator.itemgetter()方式:")
sorted_by_values_operator = sorted(my_dict.items(), key=operator.itemgetter(1))
print(sorted_by_values_operator)
print("转换为字典:", dict(sorted_by_values_operator))
print("\n" + "="*50 + "\n")

# 3. 按键降序排序
print("3. 按键降序排序:")
sorted_by_keys_reverse = sorted(my_dict.items(), reverse=True)
print(sorted_by_keys_reverse)
print("转换为字典:", dict(sorted_by_keys_reverse))
print("\n" + "="*50 + "\n")

# 4. 按值降序排序
print("4. 按值降序排序:")
print("4.1 使用lambda函数方式:")
sorted_by_values_reverse_lambda = sorted(my_dict.items(), 
                                       key=lambda x: x[1], 
                                       reverse=True)
print(sorted_by_values_reverse_lambda)
print("转换为字典:", dict(sorted_by_values_reverse_lambda))

print("\n4.2 使用operator.itemgetter()方式:")
sorted_by_values_reverse_operator = sorted(my_dict.items(), 
                                         key=operator.itemgetter(1), 
                                         reverse=True)
print(sorted_by_values_reverse_operator)
print("转换为字典:", dict(sorted_by_values_reverse_operator))
print("\n" + "="*50 + "\n")

# 5. 使用OrderedDict
print("5. 使用OrderedDict:")
print("5.1 按值排序后存入OrderedDict:")
ordered_dict = OrderedDict(sorted(my_dict.items(), key=lambda x: x[1]))
print(ordered_dict)

print("\n5.2 按值降序排序后存入OrderedDict:")
ordered_dict_reverse = OrderedDict(sorted(my_dict.items(), 
                                        key=lambda x: x[1], 
                                        reverse=True))
print(ordered_dict_reverse)
print("\n" + "="*50 + "\n")

# 6. 使用字典推导式
print("6. 使用字典推导式:")
print("6.1 按值排序:")
dict_comp_by_values = {k: v for k, v in sorted(my_dict.items(), key=lambda x: x[1])}
print(dict_comp_by_values)

print("\n6.2 按键排序:")
dict_comp_by_keys = {k: v for k, v in sorted(my_dict.items())}
print(dict_comp_by_keys)

print("\n6.3 按值降序排序:")
dict_comp_by_values_reverse = {k: v for k, v in 
                              sorted(my_dict.items(), 
                                    key=lambda x: x[1], 
                                    reverse=True)}
print(dict_comp_by_values_reverse)