def f2(m, n):
    counter = 0
    print(f"\nStarting function f2, initial values:")
    print(f"  m = {m}")
    print(f"  n = {n}")
    print(f"  counter = {counter}")
    
    while m <= n:
        print(f"\nIteration {counter+1} starts:")
        print(f"  Comparing m <= n: {m} <= {n} is {m <= n}")
        
        old_m = m
        old_n = n
        m *= 3
        n *= 2
        counter += 1
        
        print(f"  Calculation process:")
        print(f"    m: {old_m} * 3 = {m}")
        print(f"    n: {old_n} * 2 = {n}")
        print(f"    counter increased to: {counter}")
    
    print(f"\nEnd of loop condition check:")
    print(f"  m <= n: {m} <= {n} is {m <= n}")
    print(f"\nFinal result:")
    print(f"  m = {m}")
    print(f"  n = {n}")
    print(f"  counter = {counter}")
    return counter

print("Calling function f2(2, 3)")
result = f2(2, 3)
print(f"Function return value: {result}")

