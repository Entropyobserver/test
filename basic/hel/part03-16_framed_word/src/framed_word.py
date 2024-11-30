# Write your solution here
word = input("Word: ")

start = (28 - len(word)) // 2
if len(word) % 2 == 0:
    end = start
else:
    end = start+1


print('*' * 30)
print(f"*{(start * ' ')}{word}{(end * ' ')}*")
# print(f"*{word.center(28)}*")
print('*' * 30)

# 获取用户输入的单词
word = input("Word: ")
print(f"\n1. 用户输入的单词: '{word}'")
print(f"2. 单词的长度: {len(word)}")

# 计算开始位置的空格数
# 总宽度28减去单词长度，然后除以2得到一边需要的空格数
start = (28 - len(word)) // 2
print(f"\n3. 计算开始位置空格数:")
print(f"   (28 - {len(word)}) // 2 = {start}")

# 判断单词长度的奇偶性来决定结束位置的空格数
print(f"\n4. 检查单词长度是否为偶数:")
if len(word) % 2 == 0:
   print(f"   {len(word)} % 2 = 0 (偶数)")
   end = start
   print(f"   end = start = {end}")
else:
   print(f"   {len(word)} % 2 = 1 (奇数)")
   end = start + 1
   print(f"   end = start + 1 = {end}")

print("\n5. 最终的空格分配:")
print(f"   左边空格数: {start}")
print(f"   右边空格数: {end}")
print(f"   总宽度验证: {start} + {len(word)} + {end} = {start + len(word) + end}")

# 打印结果
print("\n6. 输出结果:")
print('*' * 30)
print(f"*{(start * ' ')}{word}{(end * ' ')}*")
print('*' * 30)

# 可选的替代方案（使用center方法）
print("\n7. 使用 center() 方法的替代方案:")
print(f"*{word.center(28)}*")