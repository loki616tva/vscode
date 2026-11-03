# Check whether placing a queen at the given position is safe
def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col:  # Check same column
            return False

        if abs(board[i] - col) == abs(i - row):  # Check diagonal
            return False

    return True


# Place queens row by row using backtracking
def solve(board, row):
    if row == 8:  # All 8 queens placed successfully
        return True

    for col in range(8):
        if is_safe(board, row, col):
            board[row] = col  # Place the queen

            if solve(board, row + 1):  # Solve the next row
                return True

            board[row] = -1  # Backtrack: remove the queen

    return False


# Initialize the board with no queens
board = [-1] * 8

# Print the solution if found
if solve(board, 0):
    for row in range(8):
        for col in range(8):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
else:
    print("No solution")
