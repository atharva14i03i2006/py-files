'''
SUDOKU BOARD

'''
print("   \033[1m* Sudoku Validator *   ")
print("Enter a sudoku Number(1 to 9): \n")
rowsxcolumns = 9
A = [list(map(int, input().split())) for _ in range(rowsxcolumns)]
def check_Row(A):
    check_Rows = set()
    for row in A:
        for element in row:
            if A[row][element] == A[row + 1][element + 1]:
                print("Invalid")

check_Row(A)