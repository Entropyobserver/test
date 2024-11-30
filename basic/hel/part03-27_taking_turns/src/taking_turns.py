# Write your solution here
number = int(input("Please type in a number: "))
for i in range(1, number+1):
    if i % 2 == 1:
        print(i // 2 + 1)
    else:
        print(number - i // 2 + 1)
