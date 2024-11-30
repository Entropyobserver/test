def row_correct(sudoku: list, row_no: int) -> bool:
    row = sudoku[row_no]
    numbers = [i for i in row if i!= 0]
    return len(numbers) == len(set(numbers))