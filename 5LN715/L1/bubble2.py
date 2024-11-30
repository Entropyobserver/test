def bubble(lst):
    print("\nStep 1: Starting bubble sort")
    print(f"Initial list: {lst}")
    print("----------------------------------------")
    
    for l in range(len(lst)):
        print(f"\nStep 2: Starting pass #{l+1}")
        swap = 0
        print(f"Step 3: Initialize swap flag = {swap}")
        
        for i in range(len(lst)-1):
            print(f"\nStep 4: Comparing lst[{i}] = {lst[i]} and lst[{i+1}] = {lst[i+1]}")
            
            if lst[i] > lst[i+1]:
                print(f"Step 5A: Swap needed - {lst[i]} is greater than {lst[i+1]}")
                lst[i], lst[i+1] = lst[i+1], lst[i]
                swap = 1
                print(f"After swap: {lst}")
            else:
                print(f"Step 5B: No swap needed - {lst[i]} is not greater than {lst[i+1]}")
                
        print(f"\nStep 6: End of pass #{l+1}")
        print(f"Current list state: {lst}")
        print(f"Swap flag = {swap}")
        
        if swap == 0:
            print("\nStep 7: No swaps in this pass - list is sorted!")
            print("----------------------------------------")
            break
        print("----------------------------------------")
    
    return lst

lst = [2, 3, 7, 11, 5, 13]
print("Original list:", lst)
test = bubble(lst)
print("\nFinal sorted list:", test)