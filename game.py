import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def minimax(board, depth, is_maximizing):
    if check_winner(board, "X"):
        return -10 + depth, None
    elif check_winner(board, "O"):
        return 10 - depth, None
    elif is_board_full(board):
        return 0, None

    if is_maximizing:
        max_eval = -math.inf
        best_move = None
        for i, j in get_empty_cells(board):
            board[i][j] = "O"
            eval, _ = minimax(board, depth + 1, False)
            board[i][j] = " "
            if eval > max_eval:
                max_eval = eval
                best_move = (i, j)
        return max_eval, best_move
    else:
        min_eval = math.inf
        best_move = None
        for i, j in get_empty_cells(board):
            board[i][j] = "X"
            eval, _ = minimax(board, depth + 1, True)
            board[i][j] = " "
            if eval < min_eval:
                min_eval = eval
                best_move = (i, j)
        return min_eval, best_move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)

        if turn == 0:  
            print("Human's turn")
            while True:
                try:
                    row = int(input("Enter row (0, 1, or 2): "))
                    col = int(input("Enter column (0, 1, or 2): "))
                    if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                        break
                    else:
                        print("Invalid input! Try again.")
                except ValueError:
                    print("Invalid input! Please enter a number.")

        else: 
            print("AI's turn")
            _, move = minimax(board, 0, True)
            row, col = move

        board[row][col] = players[turn]

        if check_winner(board, players[turn]):
            print_board(board)
            print("Player", players[turn], "wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        turn = (turn + 1) % 2

if __name__ == "__main__":
    main()
