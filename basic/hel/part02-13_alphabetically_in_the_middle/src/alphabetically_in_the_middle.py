letter1 = input("1st letter: ")
letter2 = input("2nd letter: ")
letter3 = input("3rd letter: ")
if letter1 < letter2 < letter3 or letter3 < letter2 < letter1:
    print("The letter in the middle is", letter2)
elif letter2 < letter1 < letter3 or letter3 < letter1 < letter2:
    print("The letter in the middle is", letter1)
else:
    print("The letter in the middle is", letter3)