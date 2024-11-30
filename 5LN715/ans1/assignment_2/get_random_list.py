import random 

def get_random(m,n):
    random_lst = []
    for i in range(n):
        random_lst.append(random.randint(0,m))
    return random_lst

if __name__ == "__main__":
    print(get_random(5,10)) 


