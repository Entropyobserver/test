import random
import time
import csv
import bubble_sort_recursive


def get_random_lst():
    random_lists = []
    for size in range(100,1100,10):
        random_list = []
        for number in range(size):
            random_list.append(random.randrange(1000))
        random_lists.append(random_list)
    return random_lists

def measure_bubble_sort():
    test_lists = get_random_lst()
    print("time,size")
    for i,test_list in enumerate(test_lists):
        size = 100 +i*10

        start_time = time.time()
        bubble_sort_recusive.bubble_sort(test_list.copy(),len(test_list))
        end_time = time.time()
        running_time = end_time - start_time
        print(f"{running_time},{size}")
#def main():
#    test = get_random_lst()
#    print(len(test))
#main()
if __name__ == "__main__":
    measure_bubble_sort()