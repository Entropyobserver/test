import re

# 定义正则表达式
pattern = r"star(t(led)?)?"

# 测试字符串
texts = ["star", "start", "started", "startled"]

# 逐个测试字符串
for text in texts:
    match = re.match(pattern, text)
    if match:
        print(f"Text: {text}")
        print("Group 0 (whole match):", match.group(0))
        if match.group(1):
            print("Group 1 (t(led)?):", match.group(1))
        if match.group(2):
            print("Group 2 (led):", match.group(2))
        print()
    else:
        print(f"Text: {text} does not match the pattern.")
