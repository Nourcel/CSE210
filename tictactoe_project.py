'''Tic tac toe Game
    Author : Nourcel Kaniki Kalonji
'''
board = [" ", " ", " ",
        " ", " ", " ",
        " ", " ", " "]

currentPlayer = "x"
RunningGame = True

def main():
    winner = None
    while RunningGame:
        display_board(board)
        Player_input(board)
        tie_check(board)
        win_check()
        player_swich()
    

def display_board(board):
    print(board[0]+ "  |  " + board[1] + "  |  " + board[2])
    print("-------------")
    print(board[3]+ "  |  " + board[4] + "  |  " + board[5])
    print("-------------")
    print(board[6]+ "  |  " + board[7] + "  |  " + board[8])
display_board(board)

def Player_input(board):
    value = int(input("selecte a number between 1 and 9: "))
    if value >= 1 and value <= 9 and board[value-1] == " ":
        board[value-1] = currentPlayer 
    else:
        print("spot not available !!!")

def horizontal_check(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != " ":
        winner = board[1]
        return True
    elif board[3] == board[4] == board[5] and board[3] != " ":
        winner = board[4]
        return True
    elif board[6] == board[7] == board[8] and board[6] != " ":
        winner = board[7]
        return True

def row_check(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != " ":
        winner = board[3]
        return True
    elif board[1] == board[4] == board[7] and board[1] != " ":
        winner = board[4]
        return True
    elif board[2] == board[5] == board[8] and board[2] != " ":
        winner = board[5]
        return True

def diagonal_check(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != " ":
        winner = board[4]
        return True
    elif board[2] == board[4] == board[6] and board[2] != " ":
        winner = board[6]
        return True

def tie_check(board):
    global RunningGame
    if " " not in board:
        display_board(board)
        print("Tied up!!!")
        RunningGame = False

def win_check():
    global RunningGame
    if horizontal_check(board) or row_check(board) or diagonal_check(board):
        print(f"The winner is {winner}")
        RunningGame = False

def player_swich():
    global currentPlayer
    if currentPlayer == "x":
        currentPlayer = "o"
    else:
        currentPlayer = "x"

if __name__ == "__main__":
    main()

    