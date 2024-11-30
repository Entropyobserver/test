def f5(a, b, c):
    print(f"\nInput parameters: a={a}, b={b}, c={c}")
    print("Step 1: Starting condition checks...")
    
    if a > b:
        print(f"Step 2: Checking condition 1: a > b ({a} > {b}) is True")
        if a > c:
            print(f"Step 3: Checking condition 2: a > c ({a} > {c}) is True")
            print(f"Step 4: Returning a = {a}")
            return a
        else:
            print(f"Step 3: Checking condition 2: a > c ({a} > {c}) is False")
            print(f"Step 4: Returning c = {c}")
            return c
    else:
        print(f"Step 2: Checking condition 1: a > b ({a} > {b}) is False")
        if b > c:
            print(f"Step 3: Checking condition 3: b > c ({b} > {c}) is True")
            print(f"Step 4: Returning b = {b}")
            return b
        else:
            print(f"Step 3: Checking condition 3: b > c ({b} > {c}) is False")
            print(f"Step 4: Returning c = {c}")
            return c

print("\nTesting f5(1, 2, 3):")
print("Result:", f5(1, 2, 3))  # Should return 3
print("\nTesting f5(1, 3, 2):")
print("Result:", f5(1, 3, 2))  # Should return 3
print("\nTesting f5(2, 1, 3):")
print("Result:", f5(2, 1, 3))  # Should return 3
print("\nTesting f5(2, 3, 1):")
print("Result:", f5(2, 3, 1))  # Should return 3
print("\nTesting f5(3, 1, 2):")
print("Result:", f5(3, 1, 2))  # Should return 3
print("\nTesting f5(3, 2, 1):")
print("Result:", f5(3, 2, 1))  # Should return 3

