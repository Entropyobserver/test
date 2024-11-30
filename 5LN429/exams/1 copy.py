"""
def f1(x):
    print(f"\nStarting function f1, parameter x = {x}")
    y = []
    print(f"Initialized empty list y = {y}")
    
    for i in range(x):
        print(f"\nOuter loop i = {i}:")
        print(f"  range({i}) = {list(range(i))}")  # Display the range of the inner loop
        
        for j in range(i):
            result = i - j
            y.append(result)
            print(f"    Inner loop j = {j}:")
            print(f"      Calculating i - j = {i} - {j} = {result}")
            print(f"      After adding to the list y = {y}")
    
    print(f"\nFunction execution completed, final result y = {y}")
    return y

print("Calling function f1(3)")
result = f1(3)
print(f"Function return value: {result}")


def f1(x):
    print("\n" + "="*50)
    print("步骤1: 函数开始执行")
    print(f"输入参数 x = {x}")
    
    print("\n步骤2: 初始化变量")
    y = []
    print(f"创建空列表 y = {y}")
    
    print("\n步骤3: 开始主循环 for i in range(x)")
    for i in range(x):
        print(f"\n  3.{i+1}) 外层循环 i = {i}")
        print(f"     准备进入内层循环")
        print(f"     内层循环将遍历 range({i}) = {list(range(i))}")
        
        print(f"\n     步骤4: 开始内层循环 for j in range({i})")
        for j in range(i):
            print(f"\n       4.{j+1}) 内层循环 j = {j}")
            
            print(f"         计算: i - j = {i} - {j}")
            result = i - j
            print(f"         计算结果: {result}")
            
            print(f"         添加结果到列表y")
            y.append(result)
            print(f"         当前列表状态: y = {y}")
    
    print("\n步骤5: 函数执行完成")
    print(f"最终列表: y = {y}")
    print("="*50)
    return y

print("\n程序开始执行")
print("调用函数: f1(3)")
result = f1(3)
print("\n程序执行完成")
print(f"函数返回值: {result}")

"""

def f1(x):
    print("\n" + "="*50)
    print("Step 1: Function starts executing")
    print(f"Input parameter x = {x}")
    
    print("\nStep 2: Initialize variables")
    y = []
    print(f"Create an empty list y = {y}")
    
    print("\nStep 3: Start the main loop for i in range(x)")
    for i in range(x):
        print(f"\n  3.{i+1}) Outer loop i = {i}")
        print(f"     Preparing to enter the inner loop")
        print(f"     The inner loop will iterate over range({i}) = {list(range(i))}")
        
        print(f"\n     Step 4: Start the inner loop for j in range({i})")
        for j in range(i):
            print(f"\n       4.{j+1}) Inner loop j = {j}")
            
            print(f"         Calculation: i - j = {i} - {j}")
            result = i - j
            print(f"         Calculation result: {result}")
            
            print(f"         Add the result to the list y")
            y.append(result)
            print(f"         Current list status: y = {y}")
    
    print("\nStep 5: Function execution completed")
    print(f"Final list: y = {y}")
    print("="*50)
    return y

print("\nProgram starts executing")
print("Calling function: f1(3)")
result = f1(3)
print("\nProgram execution completed")
print(f"Function return value: {result}")
