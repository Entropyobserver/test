def binary_search_i(data, value):
    print("初始数据:", data)
    print("要查找的值:", value)
    
    # 先对数据排序
    data = sorted(data)
    print("\n排序后的数据:", data)
    
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