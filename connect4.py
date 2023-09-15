# Define the Connect Four board
board = [[' ' for _ in range(7)] for _ in range(6)]

# Function to print the Connect Four board
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 21)

# Function to check if a player has won
def check_winner(board, player):
    # Check horizontally
    for row in board:
        for i in range(4):
            if row[i:i+4] == [player] * 4:
                return True

    # Check vertically
    for col in range(7):
        for i in range(3):
            if [board[i][col], board[i+1][col], board[i+2][col], board[i+3][col]] == [player] * 4:
                return True

    # Check diagonally (top-left to bottom-right)
    for i in range(3):
        for j in range(4):
            if [board[i][j], board[i+1][j+1], board[i+2][j+2], board[i+3][j+3]] == [player] * 4:
                return True

    # Check diagonally (bottom-left to top-right)
    for i in range(3, 6):
        for j in range(4):
            if [board[i][j], board[i-1][j+1], board[i-2][j+2], board[i-3][j+3]] == [player] * 4:
                return True

    return False

# Function to play the Connect Four game
def play_connect_four():
    player = 'X'
    while True:
        print_board(board)
        try:
            column = int(input(f"Player {player}, enter the column (0-6): "))
            if column < 0 or column > 6:
                print("Invalid column. Please choose a column between 0 and 6.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 6.")
            continue

        for i in range(5, -1, -1):
            if board[i][column] == ' ':
                board[i][column] = player
                break
            elif i == 0:
                print("Column is full. Choose another column.")
                continue

        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break

        if ' ' not in board[0]:
            print_board(board)
            print("It's a draw!")
            break

        player = 'O' if player == 'X' else 'X'

if __name__ == "__main__":
    play_connect_four()
