import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
   
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
   
    return None

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def find_winning_move(board, player):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = player
                if check_winner(board) == player:
                    board[i][j] = " "  # Undo move
                    return (i, j)
                board[i][j] = " "  # Undo move
    return None

def get_computer_move(board):
    # Check for winning move
    move = find_winning_move(board, "O")
    if move:
        return move
    
    # Check for blocking move
    move = find_winning_move(board, "X")
    if move:
        return move
    
    # Take the center if available
    if board[1][1] == " ":
        return (1, 1)

    # Take a corner if available
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    for corner in corners:
        if board[corner[0]][corner[1]] == " ":
            return corner

    # Take any remaining space
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return (i, j)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"  # X is the human player
    computer_player = "O"
   
    print("Player X goes first.")
   
    while True:
        print_board(board)
       
        if current_player == "X":
            while True:
                try:
                    row = int(input("Player X, enter the row (0-2): "))
                    col = int(input("Player X, enter the column (0-2): "))
                    if board[row][col] == " ":
                        break
                    else:
                        print("Cell is already taken! Try again.")
                except (ValueError, IndexError):
                    print("Invalid input! Please enter numbers between 0 and 2.")
        else:
            print("Computer's turn...")
            row, col = get_computer_move(board)
            print(f"Computer chooses row {row}, column {col}")

        board[row][col] = current_player
       
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
       
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break
       
        current_player = computer_player if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()