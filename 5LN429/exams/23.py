def f3(s):
    s1 = set()
    for i in range(len(s) - 2):
        x = (s[i + 2], s[i], s[i - 1], s[0])
        s1.add(x)
    return s1

print(f3("house"))
