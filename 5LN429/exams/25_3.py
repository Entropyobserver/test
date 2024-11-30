def f5(a, b, c):
    print(f"\nInput parameters: a={a}, b={b}, c={c}")
    print("Step 1: Starting condition checks...")
    
    if a >= b and a >= c:
        print(f"Step 2: Returning a = {a}")
        return a
    elif b >= a and b >= c:
        print(f"Step 2: Returning b = {b}")
        return b
    else:
        print(f"Step 2: Returning c = {c}")
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