import math

def evaluate_board(board):
    """Evaluates the board for a win or draw."""

    # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != 0:
            return board[row][0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != 0:
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]

    # Check for draw
    if all(all(cell != 0 for cell in row) for row in board):
        return 0

    return None

def minimax(board, depth, maximizing_player):
    """Implements the Minimax algorithm with Alpha-Beta Pruning."""

    winner = evaluate_board(board)
    if winner is not None:
        return winner

    if maximizing_player:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = 1
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = 0
                    max_eval = max(max_eval, eval)
        return max_eval

    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = 2
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = 0
                    min_eval = min(min_eval, eval)
        return min_eval

def get_best_move(board):
    """Finds the best move for the AI player using Minimax."""

    best_move = None
    best_eval = -math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = 1
                eval = minimax(board, 0, False)
                board[i][j] = 0
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

def print_board(board):
    """Prints the current state of the board."""

    for row in board:
        print(" | ".join(map(str, row)))
        print("-" * 9)

def play_game():
    """Plays a game of Tic-Tac-Toe against the AI."""

    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    current_player = 1  # 1 for AI, 2 for human

    while True:
        print_board(board)

        if current_player == 1:
            print("AI's turn:")
            move = get_best_move(board)
            board[move[0]][move[1]] = current_player
        else:
            print("Your turn:")
            row = int(input("Enter row number (1-3): ")) - 1
            col = int(input("Enter column number (1-3): ")) - 1
            if board[row][col] == 0:
                board[row][col] = current_player
            else:
                print("Invalid move. Try again.")
                continue

        winner = evaluate_board(board)
        if winner is not None:
            if winner == 1:
                print("AI wins!")
            elif winner == 2:
                print("You win!")
            else:
                print("It's a draw!")
            break

        current_player = 3 - current_player

if __name__ == "__main__":
    play_game()
