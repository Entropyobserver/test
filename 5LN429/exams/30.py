def f10(s):
    L = s.split()[-5:]
    d = {}
    for i in range(len(L)):
        d[(L[i], L[i-1])] = len(L[i]) + len(L[i-1])
    return d

q1 = "If we don't believe in freedom of expression for people we despise, "
q2 = "we don't believe in it at all."
q = q1 + q2  # A quote from Chomsky

print(f10(q))
