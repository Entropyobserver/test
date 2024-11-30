import random
import time
import csv
import quick_sort_recursive
import sys

def get_random_lst():
    """
    Generate a list of lists containing random integers.

    Returns:
    list: A list of lists, each containing random integers.
    """
    random_lists = []
    for size in range(100, 1100, 10):  # Loop to create lists of increasing size
        random_list = []
        for number in range(size):  # Generate random integers for each list
            random_list.append(random.randrange(1000))
        random_lists.append(random_list)  # Append the generated list to random_lists
    return random_lists

def measure_quick_sort():
    """
    Measure the time taken to sort lists using bubble sort.

    Returns:
    list: A list of dictionaries containing the time taken and the size of each list.
    """
    sys.setrecursionlimit(2000)  # Set the recursion limit to handle larger lists
    test_lists = get_random_lst()  # Generate the test lists
    results = []
    for i, test_list in enumerate(test_lists):  # Loop through each test list
        size = 100 + i * 10  # Calculate the size of the current list
        start_time = time.time()  # Record the start time
        quick_sort_recursive.quick_sort_recursive(test_list.copy())  # Sort the list using bubble sort
        end_time = time.time()  # Record the end time
        running_time = end_time - start_time  # Calculate the running time
        results.append({'time': running_time, 'size': size})  # Append the result to results
        print(f"{running_time}, {size}")  # Print the running time and size
    return results

def write_to_csv(results, output_file='quick_sort_times.csv'):
    """
    Write the results to a CSV file.

    Parameters:
    results (list): A list of dictionaries containing the time taken and the size of each list.
    output_file (str): The name of the output CSV file.
    """
    with open(output_file, 'w', newline='') as f:  # Open the file for writing
        writer = csv.DictWriter(f, fieldnames=['time', 'size'])  # Create a CSV writer object
        writer.writeheader()  # Write the header row
        writer.writerows(results)  # Write the data rows
    print("done")  # Print a completion message

if __name__ == "__main__":
    results = measure_quick_sort()  # Measure the bubble sort times
    write_to_csv(results)  # Write the results to a CSV file

