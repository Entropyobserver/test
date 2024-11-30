"""

    Define a function get_go_conj() that takes a list as input
    and output the various conjugations of "go". In the function,
    loop over the list. Use re.match() that takes two arguments:
    the regexp pattern and the loop variable.

    So the following

targets = ["go", "goes", "went", "gone", "going", "goed"]
go_conj = get_go_conj(targets)
print(get_go_conj(go_conj)==targets)

    should give

True

"""
import re

targets = ["go", "goes", "went", "gone", "going", "goed"]
def get_go_conj(lst):
    pattern = r"go(es|ne|ing|ed)?|went"
    pattern =r""
    conj = []
    for word in lst:
        if re.match(pattern,word):
            conj.append(word)
    return conj

go_conj = get_go_conj(targets)
print(get_go_conj(go_conj)==targets)


import re
def get_go_conj(lst):
    pattern = r"go(e[ds]|ne|ing)?|went"
    matches = []
    for word in lst:
        match = re.match(pattern, word)
        matches.append(match.group())
    return matches
def main():
    targets = ["go", "goes", "went", "gone", "going", "goed"]
    go_conj = get_go_conj(targets)
    print(go_conj==targets)
main()