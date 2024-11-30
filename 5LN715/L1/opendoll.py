"""
def open_doll(doll_number):
    if doll_number == 1:  # 递归终止条件
        print("This is the smallest doll.")
        return
    else:
        print(f"Opening doll {doll_number}...")
        open_doll(doll_number - 1)  # 递归调用，处理更小的套娃
        print(f"Doll {doll_number} is now fully opened.")

# 调用递归函数，假设从套娃 5 开始
"""

def open_doll(lst, n=0):
    try:
        lst[n]
        n += 1
        return open_doll(lst,n)
    except IndexError:
        return n
lst = [5,4,3,2,1]
print(open_doll(lst,0))