from collections import Counter

# 示例字典
my_dict = {'a': 2, 'b': 3, 'c': 2, 'd': 1, 'e': 3, 'f': 1, 'g': 2}
print("原始字典:")
print(my_dict)

# 方法1：使用Counter，按值的频率降序排序
print("\n方法1: 按频率降序排序")
# 统计频率
value_counts = Counter(my_dict.values())
print("值的频率:", value_counts)

# 排序并创建新字典
sorted_dict = dict(sorted(my_dict.items(), 
                         key=lambda x: value_counts[x[1]], 
                         reverse=True))
print("按频率降序的结果:", sorted_dict)

# 方法2：按频率升序，频率相同时按值排序
print("\n方法2: 按频率升序，频率相同时按值排序")
sorted_dict_asc = dict(sorted(my_dict.items(), 
                             key=lambda x: (value_counts[x[1]], x[1])))
print("按频率升序的结果:", sorted_dict_asc)

# 方法3：按频率降序，频率相同时按值排序
print("\n方法3: 按频率降序，频率相同时按值排序")
sorted_dict_desc = dict(sorted(my_dict.items(), 
                              key=lambda x: (-value_counts[x[1]], x[1])))
print("按频率降序（频率相同按值升序）的结果:", sorted_dict_desc)