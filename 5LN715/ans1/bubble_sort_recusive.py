def bubble_sort(lst, n):
    if n == 0:
        return lst
    for i in range(n-1):
        if lst[i] > lst[i+1]:
            lst[i],lst[i+1] = lst[i+1],lst[i]
    return bubble_sort(lst,n-1)

if __name__ == "__main__":
    lst = [2,52,7,1,5]
    n = len(lst)
    print(bubble_sort(lst,n))
    