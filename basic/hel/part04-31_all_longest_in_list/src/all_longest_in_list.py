
def all_the_longest(list):
    max_len = max(len(s) for s in list)
    return [s for s in list if len(s) == max_len]
if __name__ == "__main__":
    my_list = ["apple","google","facebook","microsoft"]
    result = all_the_longest(my_list)
    print(result)
