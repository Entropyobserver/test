import math

def get_log_n(n):
    if type(n) != int:
        return False
    my_logged_number = math.log(n,2)
    return my_logged_number


def main():
    for i in range(1,9):
        print(f'The base 2 log of {i} is {get_log_n(i)}')

main()
