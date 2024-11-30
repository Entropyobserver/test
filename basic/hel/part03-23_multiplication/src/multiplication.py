"""
num = int(input("Please type in a number: "))
for i in range(1,num + 1):
    for j in range(1,num + 1):
        print(f"{i} x {j} = {i*j}")
"""
num = int(input("Please type in a number: "))
print(f"\n开始生成 {num}x{num} 的乘法表...")

print("\n外层循环 i 的范围:", list(range(1, num + 1)))
print("内层循环 j 的范围:", list(range(1, num + 1)))

for i in range(1, num + 1):
    print(f"\n外层循环 i 现在是: {i}")
    for j in range(1, num + 1):
        print(f"  内层循环 j 现在是: {j}")
        print(f"  计算: {i} x {j} = {i*j}")
    print(f"第 {i} 行计算完成")

print("\n乘法表生成完成!")