import time
def tictoc(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('Elapsed time: {}'.format(end - start))
    return wrapper

@tictoc
def first_func():
    time.sleep(1)
    print('First function')

@tictoc
def second_func():
    time.sleep(2)
    print('Second function')

first_func()
second_func()
