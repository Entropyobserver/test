# Write your solution here
def everything_reversed(lst):
    return [s[::-1] for s in reversed(lst)]
if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)
