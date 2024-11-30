
def bubble_sort(lst, n):
    if n <= 1:
        return lst
    for i in range(n-1):
        if lst[i] > lst[i+1]:
            lst[i],lst[i+1] = lst[i+1],lst[i]
    return bubble_sort(lst,n-1)

if __name__ == "__main__":
    lst = [2,52,7,1,5,6,35,23,789,86,24,90,346,236,123,54,21]
    n = len(lst)
    print(bubble_sort(lst,n))

