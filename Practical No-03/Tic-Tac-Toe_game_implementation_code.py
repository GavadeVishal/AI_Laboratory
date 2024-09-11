import math

PLAYER_X = 1
PLAYER_O = -1
DRAW = 0

# Evaluate the board to determine if there is a win, loss, or draw
def evaluate(board):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != ' ':
            return PLAYER_X if board[row][0] == 'X' else PLAYER_O

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return PLAYER_X if board[0][col] == 'X' else PLAYER_O

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return PLAYER_X if board[0][0] == 'X' else PLAYER_O
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return PLAYER_X if board[0][2] == 'X' else PLAYER_O

    return DRAW if all(board[row][col] != ' ' for row in range(3) for col in range(3)) else None

# Min-Max algorithm to evaluate the best move for the current player
def min_max(board, is_max):
    score = evaluate(board)
    if score is not None:
        return score

    best = -math.inf if is_max else math.inf
    mark = 'X' if is_max else 'O'

    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = mark
                best = max(best, min_max(board, not is_max)) if is_max else min(best, min_max(board, not is_max))
                board[row][col] = ' '

    return best

# Find the best move for the 'X' player
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'X'
                move_val = min_max(board, False)
                board[row][col] = ' '
                if move_val > best_val:
                    best_move = (row, col)
                    best_val = move_val

    return best_move

# Print the board in a readable format
def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 5)

# Get the board configuration from the user
def get_board_from_user():
    print("Enter the board state (use X, O, and spaces):")
    board = []
    for i in range(3):
        while True:
            try:
                row = input(f"Enter row {i + 1} (e.g., X O X): ").strip().upper().split()
                if len(row) != 3 or any(cell not in ' XO' for cell in row):
                    raise ValueError("Invalid input. Please enter exactly 3 characters per row, using X, O, or space.")
                board.append(row)
                break
            except ValueError as e:
                print(e)
    return board

# Main code execution
board = get_board_from_user()  
print("Current board:")
print_board(board)  

best_move = find_best_move(board)  
print("Best move for X is:", best_move)  
