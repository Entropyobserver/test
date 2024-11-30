#1. re.match()
#尝试从字符串的起始位置匹配一个模式。如果匹配成功，则返回一个匹配对象；否则返回None。

import re

pattern = r'\d+'
text = '123abc'
match = re.match(pattern, text)
if match:
    print(f'Matched: {match.group()}')  # 输出: Matched: 123
else:
    print('No match')
#2. re.search()
#扫描整个字符串并返回第一个成功的匹配。如果匹配成功，则返回一个匹配对象；否则返回None。

import re

pattern = r'\d+'
text = 'abc123'
search = re.search(pattern, text)
if search:
    print(f'Found: {search.group()}')  # 输出: Found: 123
else:
    print('Not found')
AI-generated code. Review and use carefully. More info on FAQ.
#3. re.findall()
#返回字符串中所有与模式匹配的子串，结果是一个列表。如果没有找到匹配的子串，则返回空列表。

import re

pattern = r'\d+'
text = 'abc123def456'
all_matches = re.findall(pattern, text)
print(all_matches)  # 输出: ['123', '456']
AI-generated code. Review and use carefully. More info on FAQ.
4. re.split()
根据模式匹配项拆分字符串，返回一个列表。

Python

import re

pattern = r'\d+'
text = 'abc123def456'
split_result = re.split(pattern, text)
print(split_result)  # 输出: ['abc', 'def', '']
AI-generated code. Review and use carefully. More info on FAQ.
5. re.sub()
替换字符串中所有与模式匹配的子串，返回替换后的字符串。

Python

import re

pattern = r'\d+'
text = 'abc123def456'
sub_result = re.sub(pattern, 'X', text)
print(sub_result)  # 输出: 'abcXdefX'
AI-generated code. Review and use carefully. More info on FAQ.
6. re.compile()
编译正则表达式模式，返回一个模式对象，可以提高多次使用同一模式时的匹配效率。

Python

import re

pattern = re.compile(r'\d+')
text = 'abc123def456'
matches = pattern.findall(text)
print(matches)  # 输出: ['123', '456']
AI-generated code. Review and use carefully. More info on FAQ.