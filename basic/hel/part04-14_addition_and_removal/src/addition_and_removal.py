list = []
while True:
    print(f"The list is now {list}")
    choice = input("a(d)d, (r)emove or e(x)it: ")
    if choice == "d":
        if len(list) == 0:
            list.append(1)
        else:
            list.append(list[-1] + 1)
    elif choice == 'r':
        if len(list) > 0:
            list.pop()
    elif choice =='x':
        break
print("Bye!")
