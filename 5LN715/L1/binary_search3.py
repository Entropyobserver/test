def binary_search_i(data, value):
    print("初始数据:", data)
    print("要查找的值:", value)
    
    # 显示重复值的位置
    print("\n在原始数据中，值 6 的所有位置:", end=" ")
    for i, v in enumerate(data):
        if v == 6:
            print(i, end=" ")
    print()
    
    # 排序并显示排序后的位置
    data = sorted(data)
    print("\n排序后的数据:", data)
    print("在排序后的数据中，值 6 的所有位置:", end=" ")
    for i, v in enumerate(data):
        if v == 6:
            print(i, end=" ")
    print()
    
    n = len(data)
    left = 0
    right = n - 1
    step = 1
    
    while left <= right:
        middle = (left + right) // 2
        print(f"\n步骤 {step}:")
        print(f"当前搜索范围: {data[left:right+1]}")
        print(f"左边界(left) = {left}")
        print(f"右边界(right) = {right}")
        print(f"中间位置(middle) = {middle}")
        print(f"中间值 data[{middle}] = {data[middle]}")
        
        if value < data[middle]:
            print(f"目标值 {value} < 中间值 {data[middle]}, 搜索左半部分")
            right = middle - 1
        elif value > data[middle]:
            print(f"目标值 {value} > 中间值 {data[middle]}, 搜索右半部分")
            left = middle + 1
        else:
            print(f"\n找到目标值！位置为: {middle}")
            print(f"注意：这只是排序后数组中的其中一个位置")
            return middle
            
        step += 1
        
    raise ValueError('Value is not in the list')

def main():
    test = [3, 5, 46, 23, 5, 6, 634, 6, 34, 6, 7]
    try:
        result = binary_search_i(test, 6)
        print(f"\n最终结果: 值 6 在排序后数组的位置 {result}")
    except ValueError as e:
        print("\n查找失败:", str(e))

if __name__ == "__main__":
    main()