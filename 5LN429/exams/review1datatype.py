"""
num = 42
text = "Hello, World!"
my_tuple = (1, 2, 3)

# 尝试修改不可变对象会引发错误
try:
    num += 10
    print(f"Updated num: {num}")  # 输出更新后的 num
    text[0] = 'M'  # 这会引发 TypeError
    my_tuple[0] = 100  # 这也会引发 TypeError
except TypeError as e:
    print(f"Error: {e}")

# 可变对象（列表、集合、字典）
my_list = [1, 2, 3]
my_dict = {'a': 1, 'b': 2}

# 可以修改而不会有问题
my_list.append(4)
print(f"Updated my_list: {my_list}")  # 输出更新后的 my_list

del my_dict['a']
print(f"Updated my_dict: {my_dict}")  # 输出更新后的 my_dict

"""
# 初始化变量
num = 42
text = "Hello, World!"
my_tuple = (1, 2, 3)

print("初始值:")
print(f"num = {num}")
print(f"text = {text}")
print(f"my_tuple = {my_tuple}")
print("\n" + "="*50 + "\n")

# 尝试修改不可变对象
try:
    print("尝试修改不可变对象:")
    
    print("修改 num:")
    num += 10
    print(f"成功更新 num: {num}")
    
    print("\n尝试修改字符串 text:")
    print(f"当前 text = {text}")
    text[0] = 'M'  # 这会引发 TypeError
    
    print("\n尝试修改元组 my_tuple:")
    print(f"当前 my_tuple = {my_tuple}")
    my_tuple[0] = 100  # 这也会引发 TypeError
    
except TypeError as e:
    print(f"遇到类型错误: {e}")

print("\n" + "="*50 + "\n")

# 可变对象（列表、字典）
print("处理可变对象:")

my_list = [1, 2, 3]
print(f"初始列表: {my_list}")
my_list.append(4)
print(f"添加元素后的列表: {my_list}")

print("\n字典操作:")
my_dict = {'a': 1, 'b': 2}
print(f"初始字典: {my_dict}")
del my_dict['a']
print(f"删除键'a'后的字典: {my_dict}")