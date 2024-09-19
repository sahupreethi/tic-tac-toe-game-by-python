# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Function to check if a player has won
def check_win(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True

    return False

# Function to check if the board is full (a draw)
def check_draw(board):
    return all([cell != " " for row in board for cell in row])

# Function to play the game
def play_game():
    # Create an empty 3x3 board
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    # Set the current player to 'X'
    current_player = "X"
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")

        # Get the player's move
        try:
            row, col = map(int, input("Enter row and column (1-3 each, separated by space): ").split())
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a space.")
            continue

        if row not in range(1, 4) or col not in range(1, 4):
            print("Invalid move. Row and column must be between 1 and 3.")
            continue

        row, col = row - 1, col - 1  # Convert to 0-indexed
        
        if board[row][col] != " ":
            print("This cell is already taken. Try again.")
            continue

        # Place the player's move on the board
        board[row][col] = current_player

        # Check if the current player has won
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check if the game is a draw
        if check_draw(board):
            print_board(board)
            print("The game is a draw!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Start the Tic-Tac-Toe game
if __name__ == "__main__":
    play_game()
