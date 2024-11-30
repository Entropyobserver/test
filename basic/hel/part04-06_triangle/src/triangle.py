def line(n, char):
    if char == "":
        char = "*"
    print(char * n)

def triangle(size):
    for i in range(1,size + 1):
        line(i, "#")

if __name__ == "__main__":
    triangle(5)

