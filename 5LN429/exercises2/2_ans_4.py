def is_larger_than_10(x):
    if type(x) != int:
        return None
    if x > 10:
        return True
    return False

test1 = is_larger_than_10('five')
test2 = is_larger_than_10(5)
test3 = is_larger_than_10(11)

print(test1,test2,test3)
