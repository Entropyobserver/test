def linear_search_r(lst,target,n=0):
    if n >= len(lst):
        return False
    if lst[n] == target:
        return True
    return linear_search_r(lst,target,n+1)

def main():
    numbers = [4,56,23,6,7235,73]
    target = 6
    print(linear_search_r(numbers,target,0))

if __name__ == "__main__":
    main()