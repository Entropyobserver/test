def get_word_index(lst):
    print("step 2: function called")
    print("Step 3: Split the string into words")
    words = lst.split()
    print(f"Words after splitting: {words}")
    
    print("Step 4: Enumerate over the words, showing index and word")
    result = []
    for index, word in enumerate(words):
        print(f"Index: {index}, Word: {word}")
        result.append((index, word))
        print(f"Current state of result list: {result}")  # Show the result list after each append
    
    return result

# Test case
test = "This is not a Kafka quote as far as I know"
print("step 1: calling function")
print("\nFinal result:", get_word_index(test))


