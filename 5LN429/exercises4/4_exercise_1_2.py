def get_types_2(str):
    print("Input string:", str)
    set_int = set()
    set_char = set()
    for i in str:
        print("Processing character:", i)
        try:
            print("Trying to convert to int...")
            set_int.add(int(i))
            print("Added to set_int:", set_int)
        except ValueError:
            print("Cannot convert to int. Adding to set_char...")
            set_char.add(i)
            print("Added to set_char:", set_char)
    print("Final sets:")
    print("set_int:", set_int)
    print("set_char:", set_char)
    return (set_int, set_char)

print(get_types_2("somerandom342numbers3493and characters"))