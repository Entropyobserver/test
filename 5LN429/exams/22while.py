def f2(n, m):
    c = 1
    while n < m:
        n += 4
        m += 3
        c += n
    return c

print(f2(2, 4))
"""
def f3(n, m):
    c = 1
    print(f"Initial values: n = {n}, m = {m}, c = {c}")
    
    while n < m:
        n += 4
        print(f"After n += 4: n = {n}")
        
        m += 3
        print(f"After m += 3: m = {m}")
        
        c += n
        print(f"After c += n: c = {c}")
        print("-" * 30)  # Separator line for clearer output
        
    return c

print("Final result:", f3(2, 4))
"""
def f2(n, m):
    print(f"\nInitial input values: n={n}, m={m}")
    c = 1
    print(f"Step 1: Initialize c = {c}")
    
    step = 1
    while n < m:
        print(f"\nStep {step+1}: Check loop condition n < m ({n} < {m}) is True, continue loop")
        n += 4
        print(f"Step {step+1}: n += 4, new n = {n}")
        m += 3
        print(f"Step {step+1}: m += 3, new m = {m}")
        c += n
        print(f"Step {step+1}: c += n, new c = {c}")
        step += 1
    
    print(f"\nLoop ends: n < m ({n} < {m}) is False")
    print(f"Final return c = {c}")
    return c

# Test with different input values
print("\nTest f2(2, 4):")
print("Result:", f2(2, 4))

#print("\nTest f2(2, 10):")
#print("Result:", f2(2, 10))

#print("\nTest f2(3, 7):")
#print("Result:", f2(3, 7))
