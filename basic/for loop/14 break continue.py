
for i in range(5):
    for j in range(5):
        if j == 3:
            break
        if i == j:
            continue
        print(i,j)

print("开始执行嵌套循环程序")
print("外层循环的范围: range(5) =", list(range(5)))
print("内层循环的范围: range(5) =", list(range(5)))
print("\n详细执行过程:\n")

for i in range(5):
    print(f"--- 外层循环开始，i = {i} ---")
    
    for j in range(5):
        print(f"  内层循环开始，j = {j}")
        
        if j == 3:
            print(f"  检测到 j == 3，使用 break 提前退出内层循环")
            break
        
        if i == j:
            print(f"  检测到 i == j（{i} == {j}），使用 continue 跳过本次循环")
            continue
        
        print(f"  打印结果: {i} {j}")
        print(i, j)
        
        print("  内层循环继续")
    
    print(f"--- 外层循环 i = {i} 结束 ---\n")

print("程序执行完毕")