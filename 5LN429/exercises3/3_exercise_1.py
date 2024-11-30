"""

    Write a function get_char_freq() that takes one parameter as input,
    a string.

    Inside the function:
    Assign to a variable an empty dictionary. 
    Loop over the string and add key-value pairs to the dictionary,
    where the keys are the characters in the string and the values are
    the number of times the characters appear in the string.
    You can consider the punctiation mark as a character.
    Return the dictionary.

    Outside the function:
    Assign to a variable a string that contains:
    'This is a sentence that I have not constructed myself but I could have."
    Assign the function to a variable char_freq and pass in the string variable.
    Print the length of the string variable.
    Print char_freq
    Print the type of char_freq
    Print the length of char_freq 

    This should be the output:

71
{'T': 1, 'h': 4, 'i': 2, 's': 5, ' ': 13, 'a': 4, 'e': 7, 'n': 4, 't': 7, 'c': 4, 'I': 2, 'v': 2, 'o': 3, 'r': 1, 'u': 3, 'd': 2, 'm': 1, 'y': 1, 'l': 2, 'f': 1, 'b': 1, '.': 1}
<class 'dict'>
22


"""
def get_char_freq(str):
    char_dict = {}
    for i in str:
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1
    return char_dict
my_string = "This is a sentence that I have not constructed myself but I could have."
char_freq = get_char_freq(my_string)

print(len(my_string))
print(char_freq)
print(type(char_freq))
print(len(char_freq))
