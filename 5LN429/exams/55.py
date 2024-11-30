def f5(var1, var2):
    s = "bcdfghjklmnpgrstvwxz"
    lst = []
    for i in range(len(var1)):
        if var1[i][1] in s:
            lst.append((var1[i], var2[i-1]))
    return lst

a = ["the", "sun", "is", "our", "closest", "star"]
b = ["the", "second", "closest", "star", "is", "Proxima", "Centauri"]
print(f5(a, b))
