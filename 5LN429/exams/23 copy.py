def f3(s):
    print(f"输入字符串 s = '{s}'")
    print(f"字符串长度 = {len(s)}")
    print(f"循环范围 range(len(s) - 2) = range({len(s)} - 2) = range({len(s)-2})")
    
    s1 = set()
    print("创建空集合 s1 = set()")
    
    for i in range(len(s) - 2):
        print("\n" + "="*50)
        print(f"当前索引 i = {i}")
        
        # 分步骤显示每个元素的获取过程
        print(f"获取 s[i + 2] = s[{i + 2}] = '{s[i + 2]}'")
        print(f"获取 s[i] = s[{i}] = '{s[i]}'")
        print(f"获取 s[i - 1] = s[{i - 1}] = '{s[i - 1]}'")
        print(f"获取 s[0] = '{s[0]}'")
        
        x = (s[i + 2], s[i], s[i - 1], s[0])
        print(f"创建元组 x = {x}")
        
        s1.add(x)
        print(f"将元组添加到集合中，当前集合 s1 = {s1}")
    
    print("\n" + "="*50)
    print(f"最终返回集合 s1 = {s1}")
    return s1

print("\n函数执行结果:", f3("house"))