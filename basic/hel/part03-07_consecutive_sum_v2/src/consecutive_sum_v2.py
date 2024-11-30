"""
limit = int(input("Limit: "))
number = 1 
total = 1 
consecutive = "The consecutive sum: "
statement = "" 
while total < limit: 
    statement += f"{number} + "
    number += 1 
    total += number 
print(f"{consecutive} {statement}" + f"{number} = {total}")
"""
# Prompt the user to enter a limit value
limit = int(input("Limit: "))
print(f"\nThe target limit is: {limit}")

# Initialize variables
number = 1      # The current number to add, starting from 1
total = 1       # The total sum, starting at 1 (since the first number is 1)
consecutive = "The consecutive sum: "   # Prefix text for the output
statement = ""  # String to build the equation

print(f"\nInitializing variables:")
print(f"number = {number}")
print(f"total = {total}")
print(f"statement = '{statement}'")

# Continue the loop while the total is less than the limit
print("\nStarting loop:")
while total < limit:
    print(f"\n--- Loop iteration {number} ---")
    
    # Add the current number to the equation string, with a plus sign
    statement += f"{number} + "
    print(f"Adding current number to equation: statement = '{statement}'")
    
    # Increase the number by 1 for the next loop iteration
    number += 1
    print(f"Incrementing number by 1: number = {number}")
    
    # Add the new number to the total sum
    total += number
    print(f"Calculating new total: total = {total}")
    
    print(f"Checking condition: {total} < {limit} ?")

print("\nLoop ended!")
print(f"Final variable states:")
print(f"number = {number}")
print(f"total = {total}")
print(f"statement = '{statement}'")

# Print the final result
print("\nFinal output:")
print(f"{consecutive} {statement}" + f"{number} = {total}")


