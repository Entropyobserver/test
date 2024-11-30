def f3(lst):
    if type(lst) != list:
        return None
    last_chars = []
    for e in lst:
        if type(e) == str:
            last_chars.append(e[-1])
    return last_chars

print(f3("hello"))
print(f3(["wow", "3", 3, "drum"]))
