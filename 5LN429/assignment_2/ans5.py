def f5(int1,int2):
    count = 0
    while int1 < int2:
        #int1 = int1 * 3
        #int2 = int2 - 2
        int1 *= 3
        int2 -= 2
        count += 1
    return count
def g5(n):
    new_dict = {}
    for i in range(n):
        new_dict[i] = f5(i,i**2)
    return new_dict
def main():
    print(g5(20))
#if __name__ == "__main__":
#    main()
main()
