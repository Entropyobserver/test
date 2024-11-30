# Write your solution here
# You can test your function by calling it within the following block



def same_chars(string, index1, index2):
    if index1 >= len(string) or index2 >= len(string):
        return False
    return string[index1] == string[index2]

if __name__ == "__main__":
    same_chars("coder", 1, 2)
