
def categorize_by_initial(my_list):
    print("\nStep 1: Starting the categorization function...")
    print("----------------------------------------")
    groups = {}
    print("Step 2: Initialized empty dictionary groups = {}")
    print("----------------------------------------")
    
    for word in my_list:
        print(f"\nStep 3: Processing word: '{word}'")
        initial = word[0]
        print(f"Step 4: Extracted first letter: '{initial}'")
        
        # initialize a new list when the letter is first encountered
        if initial not in groups:
            print(f"Step 5A: First letter '{initial}' not in dictionary, creating new list")
            groups[initial] = []
        else:
            print(f"Step 5B: First letter '{initial}' already exists in dictionary")
            
        # add the word to the appropriate list
        groups[initial].append(word)
        print(f"Step 6: Added word '{word}' to list for '{initial}'")
        print(f"Current dictionary state: {groups}")
        print("----------------------------------------")
    
    print("\nStep 7: Categorization complete! Final result:")
    return groups

word_list = [
    "banana", "milk", "beer", "cheese", "sourmilk", "juice", "sausage",
    "tomato", "cucumber", "butter", "margarine", "cheese", "sausage",
    "beer", "sourmilk", "sourmilk", "butter", "beer", "chocolate"
]

print("Initial word list:", word_list)
groups = categorize_by_initial(word_list)

print("\nStep 8: Printing results grouped by first letter:")
for key, value in groups.items():
    print(f"\nWords starting with '{key}':")
    for word in value:
        print(f"  - {word}")