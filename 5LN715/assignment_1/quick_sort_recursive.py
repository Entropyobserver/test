def quick_sort_recursive(lst):
   if len(lst) <= 1:
       return lst
   pivot = lst[-1]
   left, right = [], []
   for x in lst[:-1]:
       if x <= pivot:
           left.append(x)
       else:
           right.append(x)
   return quick_sort_recursive(left) + [pivot] + quick_sort_recursive(right)

if __name__ =="__main__":
    lst = [9, -3, 5, 2, 6, 8, -6, 1, 3]
    print(quick_sort_recursive(lst))