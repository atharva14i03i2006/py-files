print("\033[1m* Tic Tac Toe *\033[0m")
print("\nEnter the board (X/O/_)\n")

rows = 3

board = [input().split() for _ in range(rows)]


def check_winner(board):

    # Check Rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "_":
            print(f"🎉 Player {board[i][0]} wins by Row {i+1}")
            return

    # Check Columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] != "_":
            print(f"🎉 Player {board[0][j]} wins by Column {j+1}")
            return

    # Main Diagonal
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "_":
        print(f"🎉 Player {board[0][0]} wins by Main Diagonal")
        return

    # Anti Diagonal
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "_":
        print(f"🎉 Player {board[0][2]} wins by Anti Diagonal")
        return

    # Draw or Game Continue
    for row in board:
        if "_" in row:
            print("Game is still going on.")
            return

    print("🤝 Match Draw")


check_winner(board)