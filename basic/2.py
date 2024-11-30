def number_in_list(numbers: list, target: int) -> bool:
    for number in numbers:
        if number == target:
            return True
    return False
"""
numbers: list 表示 numbers 参数应该是一个列表。
target: int 表示 target 参数应该是一个整数。
-> bool 表示函数的返回值类型应该是布尔值（True 或 False）。
"""