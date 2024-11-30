import re

def f13(pattern, lst):
    matches = []
    for s in lst:
        if re.fullmatch(pattern, s):
            matches.append(s)
    return matches

utterances = ['run', 'ruuuun', 'ruuuuuun', 'running']
weirds = ['ruuunner', 'ruuunn', 'ruunning', 'runing', 'ruunn']
#regexp = r'ru+n+(er|ing)?'
#regexp = r'^ru{1,5}n{1,2}(ing)?$'
#regexp = r'ru+n(ning)?$'
regexp = r'ru+n+ing|ru+n$'
print(f13(regexp, utterances + weirds))
print(f13(regexp, utterances + weirds) == utterances)
