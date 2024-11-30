a,b,*c,d = [1,2,3,4,5,6,7]
print(c)
"""
这行代码使用了 Python 的解包赋值语法，将列表 [1, 2, 3, 4, 5, 6, 7] 中的元素分配给变量 a、b、c 和 d。
a 被赋值为 1。
b 被赋值为 2。
*c 表示将剩余的元素 [3, 4, 5, 6] 赋值给 c，c 将成为一个列表。
d 被赋值为 7。
"""

s = 'Hello world'
#which expression correctly extracts 'H1w1'?
print(s[3:11:3])
print(s[:3:2])
print(s[::3])
print(s[3::3])