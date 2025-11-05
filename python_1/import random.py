import random

print("Welcome to Tic-Tac-Toe!")

# Variables
player_symbol = input("Do you want X or O? ").upper()
if player_symbol not in ["X", "O"]:
    print("Invalid choice! You'll be X by default.")
    player_symbol = "X"

computer_symbol = "O" if player_symbol == "X" else "X"

board = ["1","2","3","4","5","6","7","8","9"]

# Display the board with X and O updates
def display_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

# Player move
def player_move(symbol):
    while True:
        choice = input("Pick a spot (1–9): ")
        if choice not in board:
            print("That spot is already taken or invalid. Try again.")
        else:
            board[int(choice)-1] = symbol
            print(f"You placed {symbol} in spot {choice}")
            break

# Computer move
def computer_move(symbol):
    empty = [pos for pos in board if pos not in ["X","O"]]
    choice = random.choice(empty)
    board[int(choice)-1] = symbol
    print(f"Computer placed {symbol} in spot {choice}")

# Check for winner
def check_winner(symbol):
    wins = [
        [0,1,2],[3,4,5],[6,7,8], # rows
        [0,3,6],[1,4,7],[2,5,8], # cols
        [0,4,8],[2,4,6]          # diagonals
    ]
    for combo in wins:
        if all(board[i] == symbol for i in combo):
            return True
    return False

# Check for draw
def is_draw():
    return all(pos in ["X","O"] for pos in board)

# Main game loop
display_board()
while True:
    player_move(player_symbol)
    display_board()
    if check_winner(player_symbol):
        print("🎉 You win! Great job!")
        break
    if is_draw():
        print("It's a draw! 🤝")
        break

    computer_move(computer_
