# Sudoku Solver using Backtracking

# Check whether a number can be placed in a cell
def is_safe(board, row, col, num):

    # Check the given row and column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check the corresponding 3x3 box
    for i in range(3):
        for j in range(3):
            # row//3*3 and col//3*3 give the top-left corner
            # Adding i and j checks each cell inside that box
            if board[row // 3 * 3 + i][col // 3 * 3 + j] == num:
                return False

    return True


# Solve Sudoku using single possibilities and backtracking
def solve(board):

    # First, find cells having only one possible number
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                possible = []

                # Find all valid numbers for the empty cell
                for num in range(1, 10):
                    if is_safe(board, row, col, num):
                        possible.append(num)

                # If only one number is possible, place it directly
                if len(possible) == 1:
                    board[row][col] = possible[0]
                    return solve(board)

    # If no single possibility is found, use backtracking
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:

                # Try numbers from 1 to 9
                for num in range(1, 10):
                    if is_safe(board, row, col, num):
                        board[row][col] = num

                        # Recursively solve the remaining Sudoku
                        if solve(board):
                            return True

                        # Undo the choice if it leads to a dead end
                        board[row][col] = 0

                return False

    # No empty cells remain, so Sudoku is solved
    return True


# 0 represents an empty cell
board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]


# Run the solver and display the solution
if solve(board):
    print("Solution: ")
    for row in board:
        print(row)
else:
    print("No solution")

