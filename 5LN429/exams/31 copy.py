import re

def f11(pattern, lst):
    matches = []
    for s in lst:
        if re.match(pattern, s):
            matches.append(s)
    return matches  # 注意：这里修复了缩进错误，之前的return在for循环内

# 测试数据
targets = ['aaaab', 'aab', 'ab', 'aaaaab']

print("1. 测试原始数据:")
print("目标列表:", targets)

# 测试不同的正则表达式
print("\n2. 测试不同的模式:")

print("\n2.1 测试 'a*b':")
pattern1 = r'a*b'
result1 = f11(pattern1, targets)
print(f"模式 '{pattern1}' 匹配结果:", result1)
print("是否匹配所有目标:", result1 == targets)

print("\n2.2 测试 'a+b':")
pattern2 = r'a+b'
result2 = f11(pattern2, targets)
print(f"模式 '{pattern2}' 匹配结果:", result2)
print("是否匹配所有目标:", result2 == targets)

print("\n2.3 测试 'a{1,5}b':")
pattern3 = r'a{1,5}b'
result3 = f11(pattern3, targets)
print(f"模式 '{pattern3}' 匹配结果:", result3)
print("是否匹配所有目标:", result3 == targets)

print("\n2.4 测试 '^a+b$':")
pattern4 = r'^a+b$'
result4 = f11(pattern4, targets)
print(f"模式 '{pattern4}' 匹配结果:", result4)
print("是否匹配所有目标:", result4 == targets)

# 最终推荐的模式
recommended_pattern = r'a+b'
print("\n3. 最终推荐模式:")
print(f"使用模式 '{recommended_pattern}'")
final_result = f11(recommended_pattern, targets)
print("匹配结果:", final_result)
print("完全匹配:", final_result == targets)

# 解释正则表达式
print("\n4. 模式说明:")
print("""
推荐使用 'a+b' 的原因：
1. a+ 表示匹配一个或多个'a'
2. b 表示匹配一个'b'
3. 这个模式可以匹配：
   - 'ab' (一个a后跟b)
   - 'aab' (两个a后跟b)
   - 'aaaab' (多个a后跟b)
   - 'aaaaab' (任意多个a后跟b)
""")