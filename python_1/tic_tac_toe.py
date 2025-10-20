print("Hello, Tic-Tac Toe!")
player1 = "X"
player2 = "o"
print("player 1 is", player1)
print("player 2 is", player2)
print("Hello, Tic-Tac-Toe!")

# Ask player to choose
player = input("Choose your symbol (X or O): ").upper()

# Make sure player chose correctly
if player not in ["X", "O"]:
    print("Invalid choice! Defaulting to X.")
    player = "X"

# Computer gets the opposite symbol
if player == "X":
    computer = "O"
else:
    computer = "X"

# Show choices
print("Player is:", player)
print("Computer is:", computer)

# Create the game board (1–9 positions)
board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]

# Function to display the board
def display_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

# Show the board with numbers 1–9
display_board()
import random

def player_move(symbol):
    while True:
        choice = input("Choose a position (1–9): ")

        # Check if the position is valid and not taken
        if choice not in board:
            print("That spot is already taken or invalid. Try again.")
        else:
            # Place the player's symbol on the board
            board[int(choice) - 1] = symbol

            # 🎉 Fun reactions after the move
            reactions = [
                "Nice move!",
                "That’s a smart choice 😎",
                "You’re thinking ahead!",
                "Ooo... bold placement!",
                "Strategic! I see what you’re doing 👀"
            ]
            print(random.choice(reactions))
            print("Your", symbol, "is standing strong in position", choice, "⚔️")
            break

# 👇 Run this to test
display_board()
player_move("X")  # You can change "X" to "O"
display_board()
