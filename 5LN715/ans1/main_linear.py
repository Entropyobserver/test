import random
import time
import csv
import linear_search_recursive


def get_random_lst():
    random_lists = []
    for size in range(100,1100,10):
        random_list = []
        for number in range(size):
            random_list.append(random.randrange(1000))
        random_lists.append(random_list)
    return random_lists

def measure_linear_sort():
    test_lists = get_random_lst()
    print("time,size")
    for i,test_list in enumerate(test_lists):
        size = 100 +i*10

        start_time = time.time()
        linear_search_recursive.linear_search_r(test_list.copy())
        end_time = time.time()
        running_time = end_time - start_time
        print(f"{running_time},{size}")


def write_to_csv(results, output_file='linear_sort_times.csv'):
    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['time', 'size'])
        writer.writeheader()
        writer.writerows(results)
    print("done")

if __name__ == "__main__":
    results = measure_linear_sort()
    write_to_csv(results) 
