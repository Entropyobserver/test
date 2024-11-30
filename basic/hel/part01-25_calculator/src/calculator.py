n1 = float(input('Number 1: '))
n2 = float(input('Number 2: '))
operation = input('Operation: ')
if operation == 'add':
    print(f'{int(n1)} + {int(n2)} = {int(n1 + n2)}')
elif operation == 'multiply':
    print(f'{int(n1)} * {int(n2)} = {int(n1 * n2)}')
elif operation == 'subtract':
    print(f'{int(n1)} - {int(n2)} = {int(n1 - n2)}')
