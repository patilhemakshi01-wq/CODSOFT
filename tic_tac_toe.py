import random

board = [" " for _ in range(9)]

def print_board():
    print()
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
    print()

def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def player_move():
    while True:
        move = int(input("Enter position (1-9): ")) - 1
        if board[move] == " ":
            board[move] = "X"
            break
        else:
            print("Position already taken!")

def computer_move():
    # Try to win
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if check_winner("O"):
                return
            board[i] = " "
    
    # Block player
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if check_winner("X"):
                board[i] = "O"
                return
            board[i] = " "
    
    # Else random
    empty = [i for i in range(9) if board[i] == " "]
    move = random.choice(empty)
    board[move] = "O"

def game():
    print("Tic Tac Toe")
    print_board()

    for _ in range(9):
        player_move()
        print_board()
        if check_winner("X"):
            print("You win!")
            return
        
        computer_move()
        print_board()
        if check_winner("O"):
            print("Computer wins!")
            return

    print("It's a draw!")

game()
