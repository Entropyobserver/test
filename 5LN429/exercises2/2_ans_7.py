def max_of_three(a,b,c):
    if a >= b:
        if b >= c:
            return a
        if c >= a:
            return c
    if c >= b:
        return c
    return b
