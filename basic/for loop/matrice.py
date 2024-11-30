m = [[1,2,3], [4,5,6], [7,8,9]]

for i in range(len(m)): # using the number of rows in the matrix
    for j in range(len(m[i])): # using the number of items on each row
        m[i][j] += 1

print(m)

# Write your solution here
def count_matching_elements(my_matrix: list, element: int) -> int:
    count = 0
    for row in my_matrix:
        for item in row:
            if item == element:
                count += 1
    return count
if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))