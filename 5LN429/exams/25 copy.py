
"""
def f5(a, b, c):
    print(f"\n输入参数: a={a}, b={b}, c={c}")
    print("开始判断条件...")
    
    if a > b:
        print(f"条件1: a > b ({a} > {b}) 为True")
        if a > c:
            print(f"条件2: a > c ({a} > {c}) 为True")
            print(f"返回a = {a}")
            return a
        else:
            print(f"条件2: a > c ({a} > {c}) 为False")
            print(f"没有返回值，继续执行")
    else:
        print(f"条件1: a > b ({a} > {b}) 为False")
        if b < c:
            print(f"条件3: b < c ({b} < {c}) 为True")
            print(f"返回b = {b}")
            return b
        else:
            print(f"条件3: b < c ({b} < {c}) 为False")
            print(f"返回c = {c}")
            return c
    print("函数执行结束，无返回值")
    return None

print("\n测试 f5(1, 2, 3):")
print("结果:", f5(1, 2, 3))

print("\n测试 f5(1, 3, 2):")
print("结果:", f5(1, 3, 2))

print("\n测试 f5(2, 1, 3):")
print("结果:", f5(2, 1, 3))

print("\n测试 f5(2, 3, 1):")
print("结果:", f5(2, 3, 1))

print("\n测试 f5(3, 1, 2):")
print("结果:", f5(3, 1, 2))

print("\n测试 f5(3, 2, 1):")
print("结果:", f5(3, 2, 1))

def f5(a, b, c):
    print(f"\nInput parameters: a={a}, b={b}, c={c}")
    print("Starting condition checks...")
    
    if a > b:
        print(f"Condition 1: a > b ({a} > {b}) is True")
        if a > c:
            print(f"Condition 2: a > c ({a} > {c}) is True")
            print(f"Returning a = {a}")
            return a
        else:
            print(f"Condition 2: a > c ({a} > {c}) is False")
            print("No return value, continue execution")
    else:
        print(f"Condition 1: a > b ({a} > {b}) is False")
        if b < c:
            print(f"Condition 3: b < c ({b} < {c}) is True")
            print(f"Returning b = {b}")
            return b
        else:
            print(f"Condition 3: b < c ({b} < {c}) is False")
            print(f"Returning c = {c}")
            return c
    print("Function execution ended, no return value")
    return None

print("\nTesting f5(1, 2, 3):")
print("Result:", f5(1, 2, 3))

print("\nTesting f5(1, 3, 2):")
print("Result:", f5(1, 3, 2))

print("\nTesting f5(2, 1, 3):")
print("Result:", f5(2, 1, 3))

print("\nTesting f5(2, 3, 1):")
print("Result:", f5(2, 3, 1))

print("\nTesting f5(3, 1, 2):")
print("Result:", f5(3, 1, 2))

print("\nTesting f5(3, 2, 1):")
print("Result:", f5(3, 2, 1))

"""
def f5(a, b, c):
    print(f"\nInput parameters: a={a}, b={b}, c={c}")
    print("Step 1: Starting condition checks...")
    
    if a > b:
        print(f"Step 2: Checking condition 1: a > b ({a} > {b}) is True")
        if a > c:
            print(f"Step 3: Checking condition 2: a > c ({a} > {c}) is True")
            print(f"Step 4: Returning a = {a}")
            return a
        else:
            print(f"Step 3: Checking condition 2: a > c ({a} > {c}) is False")
            print("Step 4: No return value, continue execution")
    else:
        print(f"Step 2: Checking condition 1: a > b ({a} > {b}) is False")
        if b < c:
            print(f"Step 3: Checking condition 3: b < c ({b} < {c}) is True")
            print(f"Step 4: Returning b = {b}")
            return b
        else:
            print(f"Step 3: Checking condition 3: b < c ({b} < {c}) is False")
            print(f"Step 4: Returning c = {c}")
            return c
    print("Step 5: Function execution ended, returning None")
    return None

print("\nTesting f5(1, 2, 3):")
print("Result:", f5(1, 2, 3))
print("\nTesting f5(1, 3, 2):")
print("Result:", f5(1, 3, 2))
print("\nTesting f5(2, 1, 3):")
print("Result:", f5(2, 1, 3))
print("\nTesting f5(2, 3, 1):")
print("Result:", f5(2, 3, 1))
print("\nTesting f5(3, 1, 2):")
print("Result:", f5(3, 1, 2))
print("\nTesting f5(3, 2, 1):")
print("Result:", f5(3, 2, 1))

