"""
def get_char_freq(str):
    char_dict = {}
    for i in str:
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1
    return char_dict
"""
my_string = "This is a sentence that I have not constructed myself but I could have."
print(f"Original string: {my_string}")

print("\nExecuting get_char_freq function:")
char_freq = {}
for i, char in enumerate(my_string):
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1
    print(f"Step {i+1}: Processing '{char}' - Current dict: {char_freq}")

print(f"\nLength of my_string: {len(my_string)}")
print(f"\nFinal char_freq dictionary:\n{char_freq}")
print(f"\nType of char_freq: {type(char_freq)}")
print(f"\nNumber of unique characters: {len(char_freq)}")