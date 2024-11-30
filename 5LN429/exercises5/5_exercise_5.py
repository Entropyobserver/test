"""

    Use regexp. This

print(test_all("ffff123"))
print(test_all("ffff12345"))
print(test_all("ffffff1234"))
print(test_all("000000000"))
print(test_all("abcd"))

    should give this output:

True
True
True
False
False

"""
import re
def test_all(str):
    #pattern = r"\w\d"
    pattern = r"\d.*[a-zA-Z]|.*[a-zA-Z]\d"
    match = re.search(pattern,str)
    return bool(match)
print(test_all("ffff123"))
print(test_all("ffff12345"))
print(test_all("ffffff1234"))
print(test_all("000000000"))
print(test_all("abcd"))
"""
\d 表示匹配一个数字。
.* 表示匹配任意数量的任意字符（包括零个字符）。
[a-zA-Z] 表示匹配一个字母（无论是大写还是小写）。
| 是逻辑或运算符，表示匹配前面或后面的表达式。
因此，这个正则表达式可以匹配以下两种情况之一：

一个数字后面跟着任意数量的字符，然后是一个字母。
任意数量的字符后面跟着一个字母，然后是一个数字。
"""

import re


def test_all(password):
    if re.match(r'[a-z]{4,6}[0-9]{3,5}',password):
        return True
    return False


def main():
    print(test_all("ffff123"))
    print(test_all("ffff12345"))
    print(test_all("ffffff1234"))
    print(test_all("ff32982984"))
    print(test_all("000000000"))
    print(test_all("abcd"))


main()
