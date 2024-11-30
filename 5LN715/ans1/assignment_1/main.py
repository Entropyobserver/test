import random
import time
import csv
import bubble_sort_recusive
import sys

def get_random_lst():
    random_lists = []
    for size in range(100,1100,10):
        random_list = []
        for number in range(size):
            random_list.append(random.randrange(1000))
        random_lists.append(random_list)
    return random_lists

def measure_bubble_sort():
    sys.setrecursionlimit(2000)
    test_lists = get_random_lst()
    results = []
    for i,test_list in enumerate(test_lists):
        size = 100 +i*10
        start_time = time.time()
        bubble_sort_recusive.bubble_sort(test_list.copy(),len(test_list))
        end_time = time.time()
        running_time = end_time - start_time
        #results.append({running_time,size})
        results.append({'time': running_time, 'size': size})
        print(f"{running_time},{size}")
    return results

def write_to_csv(results, output_file='bubble_sort_times.csv'):
    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['time', 'size'])
        writer.writeheader()
        writer.writerows(results)
    print("done")

if __name__ == "__main__":
    results = measure_bubble_sort()
    write_to_csv(results) 