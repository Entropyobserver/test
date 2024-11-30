import random 
def get_random(m,n):
    random_lst = []
    for i in range(n):#
        random_lst.append(random.randint(0,m-1))#？
    return random_lst
if __name__ == "__main__":
    print(get_random(5,10)) 
"""
m should be used to decide the range in which a random number can be chosen
n how many such numbers should be added
m (int): The range of the random numbers (0 to m-1).上限，下限
n (int): The number of random numbers to generate.
"""

