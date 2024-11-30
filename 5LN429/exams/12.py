import re

def f12(pattern, lst):
    matches = []
    for s in lst:
        if re.match(pattern, s):
            matches.append(s)
    return matches

targets = ['steal', 'steals', 'stealing','stole','stolen']

print(f12(r'st(o(le(en)?)|eal(s|ing)?)', targets))  # True, 'stole'
print(f12(r'st(o(le(en)?)|ea(ls|ing))', targets))    # False, 'stolen'
#print(f12(r'st(o(le(en)?)|ea(ls?|ing))', targets))  # False
#print(f12(r'st(o(le(en)?)|eal(s|ing)?)', targets) == targets)  # True, 'stole'
#print(f12(r'st(o(le(en)?)|ea(ls|ing))', targets) == targets)    # False, 'stolen'
#print(f12(r'st(o(le(en)?)|ea(ls?|ing))', targets) == targets)  # False