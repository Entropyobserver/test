def f4(L):
    d = {}
    for e in L:
        if "1" in e:
            d[e[2]] = len(e)
        else:
            k = "abcd"
            s = False
            for l in e:
                if l in k:
                    s = True
            if s:
                d[e[-1]] = len(e) * len(e)
            else:
                d[e[0]] = None
    return d

print(f4(["1this", "is", "another", "1sentence"]))
