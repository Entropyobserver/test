def digit_root(n):
    while len(str(n)) > 1:  # 判断 n 是否是多位数
        digits = list(str(n))  # 将 n 转换成字符列表
        digit_sum = 0
        for digit in digits:  # 遍历 digits 列表的每一位
            digit_sum += int(digit)  # 将每个字符转换为整数并累加
        n = digit_sum  # 更新 n 为各位数的和
    return n
def digit_root(n):
    while len(str(n)) > 1:  # 判断 n 是否是多位数
        digit_sum = 0
        for digit in str(n):  # 遍历 n 的每一位
            digit_sum += int(digit)  # 将字符串转换为整数并累加
        n = digit_sum  # 更新 n 为各位数的和
    return n
print(digit_root(9785))

def digit_root(n):
    while n >= 10:  # 持续循环直到 n 是个位数
        digit_sum = 0
        for digit in str(n):  # 将 n 转换为字符串，并逐位遍历
            digit_sum += int(digit)  # 将每个字符转换为整数并累加
        n = digit_sum  # 更新 n 为各位数的和
    return n
def digit_root(n):
    while n >= 10:
        digit_sum = 0
        while n > 0:
            digit_sum += n % 10
            n //= 10
        n = digit_sum
    return n
