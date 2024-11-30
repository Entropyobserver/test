# Write your solution here
# Write your solution here
number = int(input("Please type in a number: "))

i = 1

while i <= number:
    if i+1 <= number:
        print(i+1)
    print(i)
    i += 2
# Write your solution here
number = int(input("Please type in a number: "))
print(f"\n开始程序，输入的数字是: {number}")

i = 1
print(f"初始化 i = {i}")

while i <= number:
    print(f"\n--- 当前循环开始，i = {i} ---")
    print(f"检查 i <= number: {i} <= {number} 为 True，继续循环")
    
    if i+1 <= number:
        print(f"检查 i+1 <= number: {i+1} <= {number} 为 True")
        print(f"输出 i+1: {i+1}")
        print(i+1)
    else:
        print(f"检查 i+1 <= number: {i+1} <= {number} 为 False，不输出 i+1")
    
    print(f"输出 i: {i}")
    print(i)
    
    i += 2
    print(f"i 增加 2: 新的 i = {i}")
    print(f"--- 当前循环结束 ---")

print(f"\n检查 i <= number: {i} <= {number} 为 False，程序结束")