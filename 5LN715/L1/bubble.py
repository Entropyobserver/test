def bubble(lst):
    for l in range(len(lst)):
        swap = 0
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                lst[i],lst[i+1] = lst[i+1],lst[i]  
                swap = 1
        if swap == 0:
            break
    return(lst)
lst = [2 , 3, 7, 11 ,5 ,13]
test = bubble(lst)
print(test)
"""
1.loop
Outer Loop
The outer loop dictates the number of times the list is passed through. Each pass ensures that the largest unsorted element is bubbled to its correct position. 
The amount of passes is equal to the length of the list, which in turn assures that all of the elements are sorted.

Inner Loop
The inner loop performs the comparisons and swaps of the adjacent elements. With each iteration of the outer loop, the inner loop traverses the list, comparing 
each pair of adjacent elements. If the current element is greater than the next one, they swap. This goes to the very end of the list.

第一次外层循环：
内层循环遍历整个列表，比较和交换相邻的元素。最大的元素会被移动到列表的末尾。
第二次外层循环：
内层循环再次遍历列表，但这次不包括最后一个元素，因为它已经是最大的元素。第二大的元素会被移动到倒数第二个位置。

2.
If the length of the list is n, using range(len(lst)) would generate indices from 0 to n-1. 
However, the last element at index n-1 does not have a next element to compare with, which would result in an "index out of range" error.

3.Multiple Assignment (Tuple Unpacking)
Multiple assignment allows you to assign values to multiple variables in a single line of code. 
Specifically, the line lst[i], lst[i+1] = lst[i+1], lst[i] works as follows:

Right-Hand Side Evaluation:
The right-hand side lst[i+1], lst[i] is evaluated first, creating a temporary tuple with the values of lst[i+1] and lst[i]. 
For example, if lst[i] is 7 and lst[i+1] is 5, the right-hand side creates the tuple (5, 7).

Left-Hand Side Assignment:
The values in the temporary tuple are then assigned to the variables on the left-hand side. 
So, lst[i] is assigned the value 5, and lst[i+1] is assigned the value 7.

多重赋值允许你在一行代码中同时给多个变量赋值。具体来说，lst[i], lst[i+1] = lst[i+1], lst[i] 这行代码的执行过程如下：
右侧表达式：
首先计算右侧的表达式 lst[i+1], lst[i]，并将结果存储在一个临时元组中。例如，如果 lst[i] 是 7 而 lst[i+1] 是 5，那么右侧的表达式将生成一个元组 (5, 7)。
左侧赋值：
然后将右侧元组中的值分别赋给左侧的变量。即 lst[i] 被赋值为 5，lst[i+1] 被赋值为 7。
"""