from numpy import size


def line(size, char):
    if char == "":
        char = "*"
    print(char[0]*size)

def shape(size1,char1,size2,char2):
    i = 1
    while i <= size1:
        line(i, char1)
        i += 1
    i = 1
    while i <= size2:
        line(size1,char2)
        i += 1
if __name__ == "__main__":
    shape(5, "x", 2, "o")