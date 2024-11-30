import time
import random
from scipy.stats import ttest_rel
import numpy as np
import pandas as pd
import sys

# Iterative Bubble Sort
def bubble_sort_iterative(arr):
    n = len(arr)
    for i in range(n):
        # 引入swap标志优化
        swap = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True
        # 如果没有发生交换，说明已经排序完成
        if not swap:
            break
    return arr

# Recursive Bubble Sort
def bubble_sort_recursive(arr, n=None):
    if n is None:
        n = len(arr)
    
    # 基准情况
    if n <= 1:
        return arr
    
    # 一趟冒泡
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    # 递归处理剩余部分
    return bubble_sort_recursive(arr, n - 1)

# 测量排序时间
def measure_time(func, arr):
    start = time.time()
    func(arr.copy())
    end = time.time()
    return end - start

# 生成随机列表
def generate_random_lists(sizes, num_trials=5):
    random_lists = {}
    for size in sizes:
        random_lists[size] = [
            np.random.randint(1, 1000, size).tolist() 
            for _ in range(num_trials)
        ]
    return random_lists

# 设置参数
sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
num_trials = 10

# 提高递归深度限制
sys.setrecursionlimit(2000)

# 生成随机列表
random_lists = generate_random_lists(sizes, num_trials)

# 记录时间
iterative_times = []
recursive_times = []
results = []

for size in sizes:
    size_iterative_times = []
    size_recursive_times = []
    
    for lst in random_lists[size]:
        # 测量迭代版本时间
        iterative_time = measure_time(bubble_sort_iterative, lst)
        size_iterative_times.append(iterative_time)
        
        # 测量递归版本时间  
        recursive_time = measure_time(bubble_sort_recursive, lst)
        size_recursive_times.append(recursive_time)
    
    # 记录每个尺寸的结果
    results.append({
        "size": size, 
        "iterative_avg_time": np.mean(size_iterative_times),
        "recursive_avg_time": np.mean(size_recursive_times)
    })
    
    # 收集总体时间
    iterative_times.extend(size_iterative_times)
    recursive_times.extend(size_recursive_times)

# 创建DataFrame展示结果
time_comparison = pd.DataFrame(results)
print("Time Comparison:")
print(time_comparison)

# 执行配对t检验
t_stat, p_value = ttest_rel(iterative_times, recursive_times)
print("\nPaired t-Test Results:") 
print(f"t-statistic: {t_stat}")
print(f"p-value: {p_value}")