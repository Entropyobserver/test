def f3(lst):
    # Step 1: Print the initial list
    print("Step 1: Function f3 called with list:", lst)
    
    # Step 2: Initialize an empty result list
    result = []
    print("Step 2: Initializing empty result list")
    
    # Step 3: Iterate over each item in the list
    for index, i in enumerate(lst):
        print(f"\nStep 3: Processing item {index + 1}: {i}")
        
        # Step 4: Check if the current item is a string
        print(f"Step 4: Checking if {i} is a string...")
        if isinstance(i, str):
            print(f"Step 4: {i} is a string.")
            
            # Step 5: Get the last character of the string
            last_char = i[-1]
            print(f"Step 5: Appending last character '{last_char}' to result")
            
            # Step 6: Append the last character to the result list
            result.append(last_char)
        else:
            print(f"Step 4: {i} is not a string. Skipping.")
    
    # Step 7: Print the final result list
    print("\nStep 7: Finished processing all items.")
    print("Step 7: Final result:", result)
    
    # Step 8: Return the result list
    return result

# Test the function
input_list = ["wow", "3", 3, "drum"]
print("Testing f3 with input:", input_list)
output = f3(input_list)
print("Function returned:", output)
