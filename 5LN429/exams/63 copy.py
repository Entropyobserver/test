import re

def f13(pattern, lst):
    matches = []
    for s in lst:
        if re.fullmatch(pattern, s):
            matches.append(s)
    return matches

utterances = ['run', 'ruuuun', 'ruuuuuun', 'running']
weirds = ['ruuunner', 'ruuunn', 'ruunning', 'runing', 'ruunn']

# 分析需求：
# 1. 需要匹配 utterances 中的所有词：
#    - run
#    - ruuuun
#    - ruuuuuun
#    - running
# 2. 不能匹配 weirds 中的任何词

# 正确的正则表达式应该是：
regexp = r'^ru+n$|^ru+n{1}ing$'

print(f13(regexp, utterances + weirds))
print(f13(regexp, utterances + weirds) == utterances)