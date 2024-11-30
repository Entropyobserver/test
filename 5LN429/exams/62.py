def f12(c):
    b = c.split()
    a = [x.strip('.') for x in b]
    _2 = {}
    for i in range(len(a)):
        try:
            _1 = (a[i], a[i + 2])
            if _1 in _2:
                _2[_1] += 1
            else:
                _2[_1] = 1
        except:
            print('Little darling')
    return _2

h = "sun sun sun here it comes. sun sun sun here it comes."
# Beatles lyrics
print(f12(h))
