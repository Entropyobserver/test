for i in range(3):
    for j in range(3):
        if j == 2:
            break
    else:
        print(f"Completed outer loop at i={i}")
# Demonstration of nested loops with break and else clause
# Explanation of the else clause in loops:
# - The else block executes when the inner loop completes normally (without a break)
# - If break is triggered, the else block is skipped

print("Loop Ranges:")
print("Outer loop range:", list(range(3)))
print("Inner loop range:", list(range(3)))

print("\nBeginning nested loop execution:\n")

# Outer loop iterates through range(3)
for i in range(3):
    print(f"--- Outer loop starts: i = {i} ---")
    
    # Inner loop iterates through range(3)
    for j in range(3):
        print(f"  Inner loop starts: j = {j}")
        
        # Break condition: exit inner loop when j reaches 2
        if j == 2:
            print(f"  Break condition met: j == {j}")
            print("  Exiting inner loop prematurely")
            break
        
        print("  Inner loop continues")
    
    # Else clause: executes only if inner loop completes without break
    else:
        print(f"  Completed inner loop without breaking")
        print(f"Completed outer loop at i={i}")
    
    print(f"--- Outer loop with i = {i} ends ---\n")

print("Program execution completed")