import random 

def get_random(m, n):
    random_lst = []
    for i in range(n):  # Loop n times
        random_lst.append(random.randint(0, m))  # Append a random integer between 0 and m to the list
    return random_lst

if __name__ == "__main__":
    print(get_random(5, 10))  # Generate a list of 10 random integers between 0 and 5



