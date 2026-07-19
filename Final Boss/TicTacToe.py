'''
Tic Tac Toe Game

'''

print("\033[1m* Tic Tac Toe *\033[0m")
print("\n Enter (X/O)")

rows = 3
A = [list(map(str,input().split())) for _ in range(rows)]

def check_rows(board):
    for row in board:
        seen = set()
        for element in row:
            seen.add(element)
    print(seen)
print(check_rows(A))