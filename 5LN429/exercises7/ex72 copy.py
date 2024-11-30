"""
def remove_vowels(lst):
    vowels = 'aeiou'
    result = []
    step = 1
    for word in lst:
        print(f"Step {step}: Processing word '{word}'")
        new_word = ''.join([char for char in word if char not in vowels])
        print(f"Step {step + 1}: Original word: {word}, after removing vowels: {new_word}")
        result.append(new_word)
        step += 2
    return result

test = ["this", "is", "a", "sentence"]
print("Final result:", remove_vowels(test))
"""
def remove_vowels(lst):
    vowels = 'aeiou'  # Define the vowels
    result = []
    for word in lst:
        print(f"Processing word: {word}")
        filtered_chars = [char for char in word if char not in vowels]
        print(f"Characters after removing vowels: {filtered_chars}")
        filtered_word = ''.join(filtered_chars)
        print(f"Word after joining characters: {filtered_word}")
        result.append(filtered_word)
    return result

# Test case
test = ["this", "is", "a", "sentence"]
print("Final result:", remove_vowels(test))
