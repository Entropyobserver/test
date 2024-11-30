"""
    Write a function get_types() that loops over a string and tries to
    convert each character to an integer. If it possible to convert the
    character to an integer, add that integer to a set. If not, add the
    charater to another set.

    Return both sets.

    Test case:

print(get_types("somerandom342numbers3493and characters"))
    
({9, 2, 3, 4}, {'a', 'h', 'm', 'e', 'u', 'd', 't', 'c', 'b', 'o', 'r', ' ', 's', 'n'})
"""

def get_types_1(str):
    str = str.strip().lower()
    set_int = set()
    set_char = set()
    for i in str:
        if i == type(int):
            set_int.add(int(i))
        if i == type(str):
            set_char.add(i)
    return (set_int,set_char)
print(get_types_1("somerandom342numbers3493and characters"))


def get_types_2(str):
#    str = str.strip().lower()
    set_int = set()
    set_char = set()
    for i in str:
        try:
            set_int.add(int(i))
        except ValueError:
            set_char.add(i)
    return(set_int,set_char)

print(get_types_2("somerandom342numbers3493and characters"))

