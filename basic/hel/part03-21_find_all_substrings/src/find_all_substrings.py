# Write your solution here
# Write your solution here
word = input("Please type in a word: ")
character = input("Please type in a character: ")
index = word.find(character)
while index != -1 and len(word) >= index + 3:
    print(word[index:index+3])
    index = word.find(character, index + 1)


# 获取用户输入
word = input("Please type in a word: ")
character = input("Please type in a character: ")

print(f"\n1. 初始输入:")
print(f"   单词: '{word}'")
print(f"   要查找的字符: '{character}'")
print(f"   单词长度: {len(word)}")

# 找到第一个字符出现的位置
index = word.find(character)
print(f"\n2. 首次查找字符 '{character}':")
print(f"   起始位置: index = {index}")

# 当找到字符且后面还有至少2个字符时继续循环
while index != -1 and len(word) >= index + 3:
   print(f"\n3. --- 新的循环开始 ---")
   print(f"   当前index: {index}")
   print(f"   检查条件:")
   print(f"   - index != -1: {index != -1}")
   print(f"   - len(word) >= index + 3: {len(word)} >= {index + 3} = {len(word) >= index + 3}")
   
   # 从当前位置截取3个字符
   substring = word[index:index+3]
   print(f"   截取的子串: word[{index}:{index+3}] = '{substring}'")
   print(f"   输出子串: {substring}")
   
   # 从下一个位置继续查找字符
   old_index = index
   index = word.find(character, index + 1)
   print(f"   查找下一个 '{character}':")
   print(f"   - 从位置 {old_index + 1} 开始查找")
   print(f"   - 新的index: {index}")

print(f"\n4. 循环结束:")
if index == -1:
   print(f"   原因: 没有找到更多的字符 '{character}'")
elif len(word) < index + 3:
   print(f"   原因: 剩余字符不足3个 (len(word)={len(word)}, index+3={index+3})")