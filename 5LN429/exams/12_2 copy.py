import re

def f12(pattern, lst):
    print(f"\n正则表达式模式: {pattern}")
    print(f"待匹配列表: {lst}\n")
    matches = []
    
    for s in lst:
        print(f"\n正在检查单词: {s}")
        match = re.match(pattern, s)
        
        if match:
            print(f"✓ '{s}' 匹配成功!")
            print(f"  完整匹配 (Group 0): {match.group(0)}")
            print(f"  Group 1: {match.group(1)}")
            print(f"  Group 2: {match.group(2)}")
            print(f"  Group 3: {match.group(3)}")
            print(f"  Group 4: {match.group(4)}")
            matches.append(s)
            print(f"  当前匹配列表: {matches}")
        else:
            print(f"✗ '{s}' 不匹配")
    
    print(f"\n最终匹配结果: {matches}")
    return matches

# 测试数据
pattern = r'st(o(le(en)?)|eal(s|ing)?)'
targets = ['steal', 'steals', 'stealing', 'stole', 'stolen']

print("程序开始运行...")
print("模式说明:")
print("st: 固定前缀")
print("第一个分支 o(le(en)?): 匹配 stole/stolen")
print("第二个分支 eal(s|ing)?: 匹配 steal/steals/stealing")

# 运行函数
result = f12(pattern, targets)
print("\n匹配总结:")
print(f"在 {len(targets)} 个单词中找到 {len(result)} 个匹配")
for word in result:
    match = re.match(pattern, word)
    print(f"\n单词 '{word}' 的分组详情:")
    if match:
        groups = match.groups()
        print(f"Groups: {groups}")
        print("分组解释:")
        if 'eal' in word:
            print("走 'steal' 分支:")
            print(f"- Group 1: {match.group(1)} (整个变化部分)")
            print(f"- Group 2: {match.group(2)} (eal)")
            print(f"- Group 3: {match.group(3)} (后缀)")
            print(f"- Group 4: {match.group(4)} (具体后缀)")
        else:
            print("走 'stole' 分支:")
            print(f"- Group 1: {match.group(1)} (整个变化部分)")
            print(f"- Group 2: {match.group(2)} (le部分)")
            print(f"- Group 3: {match.group(3)} (可能的en)")
            print(f"- Group 4: {match.group(4)} (None)")