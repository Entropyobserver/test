def f11(s):
    print(f"Function f11 starts processing the string: '{s}'")
    
    # Step 1: Split the string and take the first 8 words
    x = s.split()[:8]
    print(f"Step 1 - Split the string and take the first 8 words: {x}")
    print(f"  Explanation: We split the original string into a list of words and keep only the first 8 words.")
    
    z = []
    print("Step 2 - Calculate the length of each word and add it to the list z:")
    # Step 2: Append the length of each word to the list z
    for i, y in enumerate(x, 1):
        z.append(len(y))
        print(f"  2.{i} The length of the word '{y}' is {len(y)}, current z = {z}")
    
    print(f"The final result of function f11: {z}")
    return z

def g11(a):
    print(f"Function g11 starts processing the list: {a}")
    
    b = []
    print("Step 3 - Process each element in the list a:")
    # Step 3: Append elements greater than 3 (integer part) to the list b
    for i, c in enumerate(a, 1):
        print(f"  3.{i} Processing element {c}:")
        if c > 3:
            integer_part = str(c).split(".")[0]
            b.append(integer_part)
            print(f"    - {c} is greater than 3, adding its integer part '{integer_part}' to b")
        else:
            print(f"    - {c} is not greater than 3, ignoring")
        print(f"    Current b = {b}")
    
    print(f"The final result of function g11: {b}")
    return b

# Main program
print("Program starts execution")

# Step 4: Define the original string
h = "It is often safer to be in chains than to be free."
print(f"Step 4 - Original string: '{h}'")

# Step 5: Call f11 and print the result
print("\nCalling function f11")
t = f11(h)
print(f"Step 5 - Result from function f11: {t}")

# Step 6: Call g11, convert to set, and print the final result
print("\nCalling function g11")
k = set(g11(t))
print(f"Step 6 - Result from function g11 converted to set: {k}")

print("\nProgram execution completed")





"""




def f11(s):
    print(f"函数f11开始处理字符串: '{s}'")
    
    # 步骤1: 分割字符串并取前8个单词
    x = s.split()[:8]
    print(f"步骤1 - 分割字符串并取前8个单词: {x}")
    print(f"  解释: 我们将原字符串分割成单词列表，并只保留前8个单词。")
    
    z = []
    print("步骤2 - 计算每个单词的长度并添加到列表z中:")
    # 步骤2: 将每个单词的长度添加到列表z中
    for i, y in enumerate(x, 1):
        z.append(len(y))
        print(f"  2.{i} 单词 '{y}' 的长度为 {len(y)}，当前z = {z}")
    
    print(f"函数f11的最终结果: {z}")
    return z

def g11(a):
    print(f"函数g11开始处理列表: {a}")
    
    b = []
    print("步骤3 - 处理列表a中的每个元素:")
    # 步骤3: 将大于3的元素（取整数部分）添加到列表b中
    for i, c in enumerate(a, 1):
        print(f"  3.{i} 处理元素 {c}:")
        if c > 3:
            integer_part = str(c).split(".")[0]
            b.append(integer_part)
            print(f"    - {c} 大于3，添加其整数部分 '{integer_part}' 到b中")
        else:
            print(f"    - {c} 不大于3，忽略")
        print(f"    当前b = {b}")
    
    print(f"函数g11的最终结果: {b}")
    return b

# 主程序
print("程序开始执行")

# 步骤4: 定义原始字符串
h = "It is often safer to be in chains than to be free."
print(f"步骤4 - 原始字符串: '{h}'")

# 步骤5: 调用f11并打印结果
print("\n开始调用函数f11")
t = f11(h)
print(f"步骤5 - f11函数的返回结果: {t}")

# 步骤6: 调用g11，转换为集合，并打印最终结果
print("\n开始调用函数g11")
k = set(g11(t))
print(f"步骤6 - g11函数处理后的结果转换为集合: {k}")

print("\n程序执行完毕")

"""