def f9 (number):
    if number % 3 == 0:
        return True
    return False

def g9(lst):
    numbers = []
    for number in lst:
        if f9 (number):
            numbers.append(number)
    return numbers
def main():
    print(sum(g9([2,3, 4,12,15,21,40])))

main ()