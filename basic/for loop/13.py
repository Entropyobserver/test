matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = []
for row in matrix:
    new_row = []
    for elem in row:
        new_row.append(elem * 2)  # 元素操作
    result.append(new_row)
print(result)