import re
def f11(pattern,lst):
    matches = []
    for s in lst:
        if re.match(pattern,s):
            matches.append(s)
    return matches
targets = ['aaaab','aab','ab','aaaaab']
#print(f11(r'a*b',targets))
print(f11(r'a+b',targets)== targets)
#print(f11(r'ab{3}',targets))