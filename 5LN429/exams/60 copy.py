def f10a(_):
    print(f"\nStep 4 - f10a checking {_}:")
    if _ % 3 == 0:
        print(f"{_} is divisible by 3, returning True")
        return True
    print(f"{_} is not divisible by 3, returning False")
    return False

def f10b(_):
    print(f"\nStep 5 - f10b checking {_}:")
    if _ % 2 == 0:
        print(f"{_} is divisible by 2, returning False")
        return False
    print(f"{_} is not divisible by 2, returning True")
    return True

def g10(lst):
    print(f"\nStep 3 - g10 starts processing list: {lst}")
    
    print("\nCreating list of boolean values for numbers divisible by 3:")
    lst_ = []
    for x in lst:
        result = f10a(x)
        lst_.append(result)
        print(f"Processing: f10a({x}) = {result}")
    print(f"lst_ final result (divisible by 3 check): {lst_}")
    
    print("\nCreating list of odd numbers:")
    _lst = []
    for x in lst:
        if f10b(x):
            _lst.append(x)
            print(f"Number {x} is odd, adding to _lst")
    print(f"_lst final result (odd numbers): {_lst}")
    
    return _lst, lst_

def main():
    print("\nStep 1 - Program starts")
    a = [2, 3, 4, 12, 15, 21, 40]
    print(f"Step 2 - Input list initialized: a = {a}")
    
    print("\nStep 3 - Calling g10 function")
    result = g10(a)
    print(f"Step 6 - g10 returned: {result}")
    
    print(f"\nStep 7 - Calculating sum of odd numbers:")
    print(f"Odd numbers list = {result[0]}")
    sum_result = sum(result[0])
    print(f"Sum = {sum_result}")
    
    print(f"\nStep 8 - Final outputs:")
    print(f"sum(g10(a)[0]) = {sum_result}")
    print(f"g10(a)[1] = {result[1]}")

# Program Flow:
# Step 1: Program initialization
# Step 2: Input list creation
# Step 3: g10 function call begins
# Step 4: f10a calls (divisible by 3 checks)
# Step 5: f10b calls (odd number checks)
# Step 6: g10 returns results
# Step 7: Sum calculation
# Step 8: Final output display

print("=== Program Execution Begins ===")
main()
print("\n=== Program Execution Ends ===")