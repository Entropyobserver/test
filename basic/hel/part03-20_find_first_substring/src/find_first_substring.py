str = input("Please type in a word:")
char = input("Please type in a character:")
if char in str:
    index = str.index(char)
    if index <= len(str) - 3:
        print(str[index:index+3])
else:
    print(f"{char} not found in {str}")