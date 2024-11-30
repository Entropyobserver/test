import random

def generate_random_lists():
    """Generates 100 random lists of increasing lengths."""
    random_lists = []
    for size in range(100, 1100, 10):  # Start at 100, stop at 1100, step 10
        random_list = []
        for i in range(size):
            random_list.append(random.randrange(1000))
        random_lists.append(random_list)
    return random_lists


if __name__ == "__main__":
    lists = generate_random_lists()
    for i, lst in enumerate(lists[:10]):
        print(f"list {i+1} length: {len(lst)}")
        print(f"head of list: {lst[:5]}")
        print()
    print(len(lists))