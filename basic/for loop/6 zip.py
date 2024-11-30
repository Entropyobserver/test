list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for num, char in zip(list1, list2):
    for symbol in ['!', '?']:
        print(f"{num}{char}{symbol}")


print("初始列表:")
print("list1 =", [1, 2, 3])
print("list2 =", ['a', 'b', 'c'])
print("符号列表 = ['!', '?']")

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print("\n使用 zip() 组合列表:")
zipped_list = list(zip(list1, list2))
print("zip后的列表:", zipped_list)

print("\n开始执行嵌套循环:\n")

for num, char in zip(list1, list2):
    print(f"--- 外层循环开始: num = {num}, char = {char} ---")
    
    for symbol in ['!', '?']:
        print(f"  内层循环开始: symbol = {symbol}")
        print(f"  生成并打印组合: {num}{char}{symbol}")
        print(f"{num}{char}{symbol}")
        print("  内层循环继续")
    
    print(f"--- 外层循环 num = {num}, char = {char} 结束 ---\n")

print("程序执行完毕")

# The zip() function in Python is used to combine two or more iterables element-wise
# It creates an iterator of tuples where each tuple contains the corresponding elements from the input iterables
# In this example, zip() will pair elements from list1 and list2 based on their index positions
# If iterables have different lengths, zip() stops at the shortest iterable

print("Initial lists:")
print("list1 =", [1, 2, 3])
print("list2 =", ['a', 'b', 'c'])
print("Symbol list = ['!', '?']")

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

print("\nZip function demonstration:")
# Convert zip iterator to list to show the pairing
zipped_list = list(zip(list1, list2))
print("Zipped list:", zipped_list)
# Zipped result will be: [(1, 'a'), (2, 'b'), (3, 'c')]

print("\nBeginning nested loop execution:\n")

# Unpacking the zipped pairs directly in the for loop
# Each iteration assigns one element from list1 to 'num' 
# and the corresponding element from list2 to 'char'
for num, char in zip(list1, list2):
    print(f"--- Outer loop starts: num = {num}, char = {char} ---")
    
    # Inner loop iterates through symbols
    for symbol in ['!', '?']:
        print(f"  Inner loop starts: symbol = {symbol}")
        print(f"  Generate and print combination: {num}{char}{symbol}")
        print(f"{num}{char}{symbol}")
        print("  Inner loop continues")
    
    print(f"--- Outer loop with num = {num}, char = {char} ends ---\n")

print("Program execution completed")