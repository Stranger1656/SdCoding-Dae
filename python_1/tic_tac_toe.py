import random

# -------------------------
# Tic-Tac-Toe Setup
# -------------------------

print("Welcome to Tic-Tac-Toe!")

# Define player symbols
player1 = "X"
player2 = "O"
print("Player 1 is", player1)
print("Player 2 is", player2)

# Ask the player which symbol they want
player = input("Do you want X or O? ").upper()

# If they type something invalid, default to X
if player not in ["X", "O"]:
    print("That's not X or O! We'll make you X by default.")
    player = "X"

# Computer automatically gets the other symbol
computer = "O" if player == "X" else "X"
print("You are:", player)
print("The computer is:", computer)

# -------------------------
# Board Setup
# -------------------------

# Make a board with numbers 1–9
board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]

# Function to show the board
def display_board():
    print()
    print("1 | 2 | 3")
    print("--+---+--")
    print("4 | 5 | 6")
    print("--+---+--")
    print("7 | 8 | 9")
    print()

# -------------------------
# Player Move
# -------------------------

# Ask the player where they want to put their symbol
def player_move(symbol):
    while True:
        choice = input("Pick a spot to place your symbol (1–9): ")

        # Make sure the spot is valid and not already taken
        if choice not in board:
            print("That spot is taken or invalid. Try again.")
        else:
            index = int(choice) - 1
            board[index] = symbol

            # Fun messages for the player
            reactions = [
                "Nice move!",
                "Smart choice 😎",
                "Thinking ahead, I see!",
                "Bold placement!",
                "Strategic! Well played 👀"
            ]
            print(random.choice(reactions))
            print("Your", symbol, "is now in position", choice, "⚔️")
            break

# -------------------------
# Computer Move
# -------------------------

# Let the computer randomly pick an empty spot
def computer_move(symbol):
    empty_positions = [pos for pos in board if pos not in ["X", "O"]]
    choice = random.choice(empty_positions)
    index = int(choice) - 1
    board[index] = symbol
    print("The computer placed", symbol, "in position", choice, "🤖")

# -------------------------
# Check Winner or Draw
# -------------------------

# Check if a player or computer has won
def check_winner(symbol):
    # All the possible winning combinations
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == symbol for i in condition):
            return True
    return False

# Check if the board is full (draw)
def is_draw():
    return all(pos in ["X","O"] for pos in board)

# -------------------------
# Game Loop
# -------------------------

display_board()  # Show the starting board

while True:
    # Player takes a turn
    player_move(player)
    display_board()
    if check_winner(player):
        print("You win! 🎉 Congratulations!")
        break
    if is_draw():
        print("It's a draw! 🤝 Well played.")
        break

    # Computer takes a turn
    computer_move(computer)
    display_board()
    if check_winner(computer):
        print("The computer wins! 🤖 Better luck next time.")
        break
    if is_draw():
        print("It's a draw! 🤝 Well played.")
        break

print("Game over. Thanks for playing! 🎮")
