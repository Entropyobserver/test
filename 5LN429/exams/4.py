def f4(string):
    string[1] = "u"
    return string
print(f4("cat"))

#TypeError: 'str' object does not support item assignment 字符串是不可变的对象。这意味着一旦创建了字符串，就不能修改它的内容。

def f4_2(string):
    new_string = string[:1] + "u" + string[2:]
    return new_string

print(f4_2("cat"))
