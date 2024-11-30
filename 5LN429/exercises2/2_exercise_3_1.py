def f3(lst):
    print(f"Function f3 called with list: {lst}")
    result = []
    print("Initializing empty result list")
    
    for index, i in enumerate(lst):
        print(f"\nProcessing item {index + 1}: {i}")
        print(f"Checking if {i} is a string...")
        
        if isinstance(i, str):
            print(f"{i} is a string.")
            last_char = i[-1]
            print(f"Appending last character '{last_char}' to result")
            result.append(last_char)
        else:
            print(f"{i} is not a string. Skipping.")
    
    print(f"\nFinished processing all items.")
    print(f"Final result: {result}")
    return result

# Test the function
input_list = ["wow", "3", 3, "drum"]
print("Testing f3 with input:", input_list)
output = f3(input_list)
print("Function returned:", output)