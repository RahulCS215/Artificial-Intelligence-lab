
import math

def printBoard(board):
    for row in board:
        print(" | ".join(cell if cell != "" else " " for cell in row))
        print("-" * 9)

def evaluateBoard(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "":
            return 10 if row[0] == 'X' else -10
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "":
            return 10 if board[0][col] == 'X' else -10
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return 10 if board[0][0] == 'X' else -10
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return 10 if board[0][2] == 'X' else -10
    return 0

def isDraw(board):
    for row in board:
        if "" in row:
            return False
    return True

def minimax(board, depth, isMaximizing):
    score = evaluateBoard(board)
    if score == 10 or score == -10:
        return score
    if isDraw(board):
        return 0

    if isMaximizing:
        bestScore = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ""
                    bestScore = max(bestScore, score)
        return bestScore
    else:
        bestScore = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ""
                    bestScore = min(bestScore, score)
        return bestScore

def findBestMove(board):
    bestValue = -math.inf
    bestMove = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = 'X'
                moveValue = minimax(board, 0, False)
                board[i][j] = ""
                if moveValue > bestValue:
                    bestMove = (i, j)
                    bestValue = moveValue
    return bestMove

def playGame():
    board = [["" for _ in range(3)] for _ in range(3)]
    print("Tic Tac Toe!")
    print("You are 'O'. The AI is 'X'.")
    printBoard(board)

    while True:
        while True:
            try:
                row, col = map(int, input("Enter your move (row and column: 0, 1, or 2): ").split())
                if board[row][col] == "":
                    board[row][col] = 'O'
                    break
                else:
                    print("Cell is already taken. Choose another.")
            except (ValueError, IndexError):
                print("Invalid input. Enter row and column as two numbers between 0 and 2.")

        print("Your move:")
        printBoard(board)

        if evaluateBoard(board) == -10:
            print("You win!")
            break
        if isDraw(board):
            print("It's a draw!")
            break

        print("AI is making its move...")
        bestMove = findBestMove(board)
        board[bestMove[0]][bestMove[1]] = 'X'

        print("AI's move:")
        printBoard(board)

        if evaluateBoard(board) == 10:
            print("AI wins!")
            break
        if isDraw(board):
            print("It's a draw!")
            break

playGame()
