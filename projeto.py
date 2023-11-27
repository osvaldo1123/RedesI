# game_logic.py
def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def make_move(board, row, col, player):
    if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
        board[row][col] = player
        return True
    return False

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)


def check_win(board, player):
    # Verifica linhas e colunas
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    # Verifica diagonais
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def check_draw(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))
