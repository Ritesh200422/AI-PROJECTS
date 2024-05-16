import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

currentPlayer = "X"
winner = None
gameRunning = True


# PRINTING THE BOARD
def printboard ( board ):
    print( board[0] + " | " + board[1] + " | " + board[2])

    print("---------")

    print(board[3] + " | " + board[4] + " | " + board[5])

    print("---------")

    print(board[6] + " | " + board[7] + " | " + board[8])

# TAKING PLAYER INPUT

def playerInput( board ):

    value = int(input("Enter the number from 1 - 9 : "))

    if value >= 1 and value <= 9 and board[value - 1] == "-":

        board[value - 1] = currentPlayer

    else:

        print("This spot is already used !!! ")

# CHECK FOR WIN OR TIE

def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner =board[0]
        return True

    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner =board[3]
        return True

    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner =board[6]
        return True

def checkVerticle(board):
    global  winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner =board[0]
        return True

    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner =board[1]
        return True

    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner =board[2]
        return True

def checkDiagonal(board):
    global winner

    if board[0] == board[4] == board[8] and board[0] != "-":
        winner =board[0]
        return True

    elif board[2] == board[4] == board[8] and board[2] != "-":
        winner =board[2]
        return True

def checkTie(board):
    if "-" not in board:
        printboard(board)
        print("It is a Tie!! ")
        gameRunning =False


# SWITCH PLAYER

def switchPlayer():

    global currentPlayer

    if currentPlayer == "X":

        currentPlayer = "O"
    else:
        currentPlayer = "X"

# CHECK FOR WIN OR TIE

def checkWin():
    if checkDiagonal(board) or checkHorizontal(board) or checkVerticle(board):
        print(f"The Winner Is  {winner}")

def comupter(board):
    while currentPlayer == "O":
        position  =random.randint(0,8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()




while gameRunning:
    printboard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()

    comupter(board)
    checkWin()
    checkTie(board)






