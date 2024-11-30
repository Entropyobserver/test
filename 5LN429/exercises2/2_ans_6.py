def times_five(n):
    if type(n) == int:
        return n*5


def also_times_five(m):
    if type(m) == int:
        first = times_five(m)
        return first*5
    return None

print(times_five("the"))
print(also_times_five(5))
