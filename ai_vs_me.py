import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

currentPlayer = "X"
winner = None
gameRunning = True

# PRINTING THE BOARD
def printboard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# TAKING PLAYER INPUT
def playerInput(board):
    value = int(input("Enter the number from 1 - 9 : "))
    if value >= 1 and value <= 9 and board[value - 1] == "-":
        board[value - 1] = currentPlayer
    else:
        print("This spot is already used or invalid input!")

# CHECK FOR WIN OR TIE
def check_win(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    elif board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    elif board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    return False

def check_tie(board):
    return "-" not in board

# SWITCH PLAYER
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

# MINIMAX ALGORITHM
def minimax(board, depth, is_maximizing):
    if check_win(board):
        if winner == "X":
            return -10 + depth, None
        elif winner == "O":
            return 10 - depth, None
        else:
            return 0, None
    elif check_tie(board):
        return 0, None

    if is_maximizing:
        best_score = float('-inf')
        best_move = None
        for i in range(9):
            if board[i] == "-":
                board[i] = "O"
                score, _ = minimax(board, depth + 1, False)
                board[i] = "-"
                if score > best_score:
                    best_score = score
                    best_move = i
        return best_score, best_move
    else:
        best_score = float('inf')
        best_move = None
        for i in range(9):
            if board[i] == "-":
                board[i] = "X"
                score, _ = minimax(board, depth + 1, True)
                board[i] = "-"
                if score < best_score:
                    best_score = score
                    best_move = i
        return best_score, best_move

def strongest_opponent(board):
    _, move = minimax(board, 0, True)
    if move is not None:
        board[move] = "O"

while gameRunning:
    printboard(board)
    playerInput(board)
    if check_win(board):
        printboard(board)
        print(f"The winner is {winner}!")
        break
    if check_tie(board):
        printboard(board)
        print("It's a tie!")
        break
    switchPlayer()
    strongest_opponent(board)
    if check_win(board):
        printboard(board)
        print(f"The winner is {winner}!")
        break
    if check_tie(board):
        printboard(board)
        print("It's a tie!")
        break
    switchPlayer()
