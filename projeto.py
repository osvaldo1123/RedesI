def init_tab():
    return [[' ' for _ in range(3)] for _ in range(3)]

def faz_mov(tabuleiro, linha, col, jogador):
    if 0 <= linha < 3 and 0 <= col < 3 and tabuleiro[linha][col] == ' ':
        tabuleiro[linha][col] = jogador
        return True
    return False

def print_tabuleiro(tabuleiro):
    for i, linha in enumerate(tabuleiro):
        print(" | ".join(linha))
        if i < 2:
            print("-" * 9)


def check_vitoria(tabuleiro, jogador):
    # Verifica linhas e colunas
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)) or all(tabuleiro[j][i] == jogador for j in range(3)):
            return True

    # Verifica diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True

    return False

def check_empate(tabuleiro):
    return all(tabuleiro[i][j] != ' ' for i in range(3) for j in range(3))
