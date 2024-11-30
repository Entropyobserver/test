def f7(a, b):
    print(f"\n开始执行f7函数")
    print(f"输入参数: a = {a}")
    print(f"输入参数: b = {b}")
    L = []
    print(f"初始化空列表 L = {L}")
    
    for index, i in enumerate(a):
        print(f"\n第{index+1}步: 处理元素 i = {i}")
        try:
            print(f"  尝试将 {i} 转换为整数")
            x = int(i)
            print(f"  转换成功: x = {x}")
            if x in b:
                print(f"  {x} 在列表b中")
                L.append(x)
                print(f"  将 {x} 添加到L中, 现在 L = {L}")
            else:
                print(f"  {x} 不在列表b中,跳过")
        except:
            print(f"  转换失败,调用g7函数处理 {i}")
            result = g7(i)
            print(f"  g7({i})返回值为 {result}")
            L.append(result)
            print(f"  将 {result} 添加到L中, 现在 L = {L}")
    
    print(f"\n完整列表 L = {L}")
    final_result = L[:-3]
    print(f"返回去掉后三个元素的列表: {final_result}")
    return final_result

def g7(y):
    print(f"\n  开始执行g7函数,参数 y = {y}")
    c = 0
    print(f"  初始化计数器 c = {c}")
    for index, e in enumerate(y):
        c += 1
        print(f"  第{index+1}个字符: {e}, c增加1, 现在 c = {c}")
    print(f"  g7函数返回 c = {c}")
    return c

L1 = [1, "Newton", "9", "left", 0, "the", "ghost", "intact", "2"]
L2 = ["9", "1", 1, "ghost", 2]

print("\n测试 f7(L1, L2):")
print("最终结果:", f7(L1, L2))
