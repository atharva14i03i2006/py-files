print("\033[1m* Sudoku Validator *\033[0m")
print("Enter the Sudoku Board (9 rows, each with 9 numbers)")
print("Use 0 for empty cells.\n")

rows = 9

A = [list(map(int, input().split())) for _ in range(rows)]


def check_rows(board):
    for row in board:
        seen = set()
        for element in row:
            if element == 0:
                continue
            if element in seen:
                return False
            seen.add(element)
    return True


def check_columns(board):
    for col in range(9):
        seen = set()
        for row in range(9):
            element = board[row][col]
            if element == 0:
                continue
            if element in seen:
                return False
            seen.add(element)
    return True


def check_boxes(board):
    for start_row in range(0, 9, 3):
        for start_col in range(0, 9, 3):

            seen = set()

            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):

                    element = board[i][j]

                    if element == 0:
                        continue

                    if element in seen:
                        return False

                    seen.add(element)

    return True


if check_rows(A) and check_columns(A) and check_boxes(A):
    print("\n✅ Sudoku is Valid")
else:
    print("\n❌ Sudoku is Invalid")