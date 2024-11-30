num = int(input('Please type in a number: '))
if num < 1000:
    print(f'This number is smaller than 1000')
    print("This number is smaller than 100")
    print("This number is smaller than 10")
    
elif 100 <num < 1000:
    print(f'This number is smaller than 100')
    print("This number is smaller than 10")
    
elif 10 <num < 100:
    print(f'This number is smaller than 10')
print('Thank you!')