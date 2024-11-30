import re

# 定义正则表达式
pattern = re.compile(r'star(t(led)?)?')

# 测试字符串
test_strings = ["star", "start", "started", "startled"]

# 匹配并打印结果
for test in test_strings:
    match = pattern.match(test)
    if match:
        print(match.group())
