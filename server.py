import socket
from projeto import initialize_board, make_move, print_board, check_win, check_draw

SERVER_IP = '127.0.0.1'
SERVER_PORT = 5555
BUFFER_SIZE = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen()

print(f"Servidor aguardando conexões em {SERVER_IP}:{SERVER_PORT}")

# Aceita o cliente
client_socket, client_address = server_socket.accept()
print(f"Conexão recebida de {client_address}")

# Inicializa o tabuleiro
board = initialize_board()

# Inicializa o símbolo do jogador
player_symbol = 'X'

while not (check_win(board, player_symbol) or check_draw(board)):
    # Envia o estado do tabuleiro para o cliente
    board_str = "\n".join(" | ".join(row) for row in board)
    client_socket.send(board_str.encode('utf-8'))

    # Aguarda a jogada do jogador
    move = client_socket.recv(BUFFER_SIZE).decode('utf-8').split(',')
    row, col = map(int, move)

    if make_move(board, row, col, player_symbol):
        if check_win(board, player_symbol):
            print_board(board)
            client_socket.send("Vitoria".encode('utf-8'))
            break
        elif check_draw(board):
            print_board(board)
            client_socket.send("Empate".encode('utf-8'))
            break

    player_symbol = 'O' if player_symbol == 'X' else 'X'

board_str = "\n".join(" | ".join(row) for row in board)
client_socket.send(board_str.encode('utf-8'))

# Fecha a conexão
client_socket.close()
server_socket.close()
