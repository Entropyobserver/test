
"""
import math

def calculate_equation_with_steps(x):

    #Calculate equation with detailed steps for both cases where len(x) >= 13 and len(x) < 13
   
    n = len(x)
    total_sum = 0
    print(f"\n计算过程 - 输入列表长度: {n}")
    print(f"n = {n}")
    iterations = min(13, n)
    print(f"min(13, n) = min(13, {n}) = {iterations}")
    print("\n各项详细计算过程:")
    
    for i in range(iterations):
        xi = x[i]
        if xi != 0:
            # 计算 (xi - xi^3)^2
            cube = xi ** 3
            diff = xi - cube
            square_diff = diff ** 2
            
            # 计算 sqrt(xi)
            sqrt_xi = math.sqrt(xi)
            
            # 计算完整项
            term = square_diff * (n-1) / sqrt_xi
            
            # 打印详细步骤
            print(f"\n第{i+1}项 (i={i}, xi={xi}):")
            print(f"  1. xi^3 = {xi}^3 = {cube}")
            print(f"  2. (xi - xi^3) = ({xi} - {cube}) = {diff}")
            print(f"  3. (xi - xi^3)^2 = ({diff})^2 = {square_diff}")
            print(f"  4. √xi = √{xi} = {sqrt_xi:.4f}")
            print(f"  5. (n-1) = {n-1}")
            print(f"  6. 最终项 = {square_diff} * {n-1} / {sqrt_xi:.4f} = {term:.4f}")
            
            total_sum += term
            print(f"  当前总和: {total_sum:.4f}")
    
    print(f"\n最终结果: {total_sum:.4f}")
    return total_sum

# 测试情况1：长度大于等于13的情况
print("情况1：长度大于等于13的列表")
long_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
result1 = calculate_equation_with_steps(long_list)

# 测试情况2：长度小于13的情况
print("\n\n情况2：长度小于13的列表")
short_list = [1, 2, 3, 4, 5]
result2 = calculate_equation_with_steps(short_list)

# 比较两种情况的结果
print("\n\n结果比较:")
print(f"长列表结果: {result1:.4f}")
print(f"短列表结果: {result2:.4f}")
"""

import math

def calculate_equation_with_steps(x):
    """
    Calculate equation with detailed steps for both cases where len(x) >= 13 and len(x) < 13
    """
    print("\nStep 1: Initialize variables")
    n = len(x)
    total_sum = 0
    print(f"  • List length n = {n}")
    print(f"  • Initial total_sum = {total_sum}")
    
    print("\nStep 2: Determine number of iterations")
    iterations = min(13, n)
    print(f"  • min(13, n) = min(13, {n}) = {iterations}")
    
    print("\nStep 3: Begin main calculation loop")
    for i in range(iterations):
        print(f"\n--- Loop iteration {i+1} ---")
        xi = x[i]
        print(f"Step 3.1: Get current value xi = x[{i}] = {xi}")
        
        if xi != 0:
            print(f"Step 3.2: Calculate components for xi = {xi}")
            
            # Step 3.2.1: Calculate cube
            cube = xi ** 3
            print(f"  • Step 3.2.1: xi^3 = {xi}^3 = {cube}")
            
            # Step 3.2.2: Calculate difference
            diff = xi - cube
            print(f"  • Step 3.2.2: (xi - xi^3) = ({xi} - {cube}) = {diff}")
            
            # Step 3.2.3: Calculate square of difference
            square_diff = diff ** 2
            print(f"  • Step 3.2.3: (xi - xi^3)^2 = ({diff})^2 = {square_diff}")
            
            # Step 3.2.4: Calculate square root
            sqrt_xi = math.sqrt(xi)
            print(f"  • Step 3.2.4: sqrt(xi) = sqrt({xi}) = {sqrt_xi:.4f}")
            
            # Step 3.2.5: Calculate multiplier
            multiplier = n - 1
            print(f"  • Step 3.2.5: (n-1) = {multiplier}")
            
            # Step 3.2.6: Calculate final term
            term = square_diff * multiplier / sqrt_xi
            print(f"  • Step 3.2.6: Final term = {square_diff} * {multiplier} / {sqrt_xi:.4f} = {term:.4f}")
            
            # Step 3.2.7: Add to total sum
            old_sum = total_sum
            total_sum += term
            print(f"  • Step 3.2.7: Update total_sum: {old_sum:.4f} + {term:.4f} = {total_sum:.4f}")
        else:
            print(f"  • Skip calculation for xi = 0")
    
    print("\nStep 4: Return final result")
    print(f"Final total_sum = {total_sum:.4f}")
    return total_sum

print("\nSTART PROGRAM")
print("=" * 50)

print("\nTEST CASE 1: Long List")
print("-" * 30)
long_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(f"Input list: {long_list}")
result1 = calculate_equation_with_steps(long_list)

print("\nTEST CASE 2: Short List")
print("-" * 30)
short_list = [1, 2, 3, 4, 5]
print(f"Input list: {short_list}")
result2 = calculate_equation_with_steps(short_list)

print("\nFINAL RESULTS COMPARISON")
print("=" * 50)
print(f"Long list result:  {result1:.4f}")
print(f"Short list result: {result2:.4f}")
print("\nEND PROGRAM")
