# Step 2: Displaying the Game Board
def display_board(board):
    print("\n  0   1   2")
    for index, row in enumerate(board):
        print(f"{index} " + " | ".join(row))
        if index < 2:
            print("  ---------")
    print("\n")

# Step 3: Getting Player Input
def player_input(board, player):
    while True:
        try:
            print(f"Player {player}'s turn.")
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            
            # Validate input range
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input. Please enter 0, 1, or 2.")
            # Validate if the cell is empty
            elif board[row][col] != " ":
                print("That space is already taken! Choose an empty square.")
            else:
                return row, col
        except ValueError:
            print("Invalid input. Please enter numbers only.")

# Step 4: Checking for a Winner
def check_win(board, player):
    # Check horizontal rows
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True
            
    # Check vertical columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
            
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
        
    return False

# Step 5: Checking for a Tie
def check_tie(board):
    for row in board:
        if " " in row:
            return False  # An empty space exists, so it's not a tie yet
    return True  # No empty spaces left

# Step 6: The Main Game Loop
def play():
    # Step 1: Representing the Game Board
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    
    current_player = "X"
    print("Welcome to Tic Tac Toe!")
    
    while True:
        display_board(board)
        
        # Get the current player's input
        row, col = player_input(board, current_player)
        
        # Update the board with the player's move
        board[row][col] = current_player
        
        # Check for a winner
        if check_win(board, current_player):
            display_board(board)
            print(f"Congratulations! Player {current_player} wins!")
            break
            
        # Check for a tie
        if check_tie(board):
            display_board(board)
            print("Game over! It's a tie!")
            break
            
        # Switch to the next player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

# Start the game
if __name__ == "__main__":
    play()