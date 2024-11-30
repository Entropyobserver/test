def line(n, char):
    if char == "":
        char = "*"
    print(char * n)

def square(side_length,char):
    for i in range(side_length):
        line(side_length, char)

if __name__ == "__main__":
    square(5,"!")
