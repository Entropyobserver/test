def f11(s):
    # Step 1: Split the string and take the first 8 words
    x = s.split()[:8]
    print(f"Step 1 - After splitting and slicing: {x}")
    
    z = []
    # Step 2: Append the length of each word to the list z
    for y in x:
        z.append(len(y))
        print(f"Step 2 - Appending length of '{y}': {len(y)} -> {z}")
    
    return z

def g11(a):
    b = []
    # Step 3: Append elements greater than 3 to the list b after processing
    for c in a:
        if c > 3:
            b.append(str(c).split(".")[0])
            print(f"Step 3 - Appending '{str(c).split('.')[0]}' from {c} -> {b}")
    
    return b

# Step 4: Define the original string
h = "It is often safer to be in chains than to be free."
print(f"Step 4 - Original string: {h}")

# Step 5: Call f11 and print the result
t = f11(h)
print(f"Step 5 - Result from f11: {t}")

# Step 6: Call g11, convert to set, and print the final result
k = set(g11(t))
print(f"Step 6 - Result from g11 (set): {k}")
"""

def f11(s):
    x = s.split()[:8]
    print(f"After splitting and slicing: {x}")
    z = []
    for y in x:
        z.append(len(y))
        print(f"Appending length of '{y}': {len(y)} -> {z}")
    return z

def g11(a):
    b = []
    for c in a:
        if c > 3:
            b.append(str(c).split(".")[0])
            print(f"Appending '{str(c).split('.')[0]}' from {c} -> {b}")
i    return b

h = "It is often safer to be in chains than to be free."
print(f"Original string: {h}")
t = f11(h)
print(f"Result from f11: {t}")
k = set(g11(t))
print(f"Result from g11 (set): {k}")
"""