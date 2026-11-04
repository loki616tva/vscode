def minimax(board, isMax):
    if "X" in board and board.count("X") == 3:
        return 1
    if "O" in board and board.count("O") == 3:
        return -1
    if " " not in board:
        return 0

    best = -999 if isMax else 999

    for i in range(9):
        if board[i] == " ":
            board[i] = "X" if isMax else "O"
            score = minimax(board, not isMax)
            board[i] = " "

            best = max(best, score) if isMax else min(best, score)

    return best

board = [" "] * 9

for i in range(9):
    print("X" if i % 2 == 0 else "O")
    if i % 2 == 0:
        best, move = -999, -1
        for j in range(9):
            if board[j] == " ":
                board[j] = "X"
                score = minimax(board, False)
                board[j] = " "
                if score > best:
                    best, move = score, j
        board[move] = "X"
    else:
        move = int(input("Enter position (0-8): "))
        board[move] = "O"

    for j in range(0, 9, 3):
        print(board[j:j+3])