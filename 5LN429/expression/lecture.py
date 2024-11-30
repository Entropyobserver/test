def get_vowels(word):
    return [char for char in word if char in "aeioy"]
my_word = "gergoqeD"
print(f"The vowels of the word {my_word} are:",".".join(get_vowels(my_word)))