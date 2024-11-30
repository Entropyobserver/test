def f5(var1, var2):
    s = "bcdfghjklmnpgrstvwxz"
    lst = []
    print("Initial data:")
    print(f"var1 = {var1}")
    print(f"var2 = {var2}")
    print(f"\nConsonant set s = {s}")
    
    for i in range(len(var1)):
        print(f"\n--- Loop {i+1} ---")
        print(f"Current word from var1[{i}] = {var1[i]}")
        
        if len(var1[i]) > 1:
            second_letter = var1[i][1]
            print(f"Second letter is: {second_letter}")
            
            if second_letter in s:
                print(f"Second letter {second_letter} is a consonant")
                prev_word = var2[i-1] if i > 0 else var2[0]
                print(f"Getting previous word from var2[{i-1}] = {prev_word}")
                
                new_tuple = (var1[i], prev_word)
                print(f"Adding new tuple: {new_tuple}")
                lst.append((var1[i], var2[i-1]))
            else:
                print(f"Second letter {second_letter} is not a consonant, skipping")
                
        print(f"Current list content: {lst}")
    
    print("\nFinal result:")
    return lst

# Test code
a = ["the", "sun", "is", "our", "closest", "star"]
b = ["the", "second", "closest", "star", "is", "Proxima", "Centauri"]
print("Final output:", f5(a, b))