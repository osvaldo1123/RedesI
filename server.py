import socket
from projeto import init_tab, faz_mov, print_tabuleiro, check_vitoria, check_empate

SERVER_IP = '127.0.0.1'
SERVER_PORT = 5555
BUFFER_SIZE = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen()

print(f"Servidor aguardando conexões em {SERVER_IP}:{SERVER_PORT}")

# Aceita o cliente
client_socket, client_adr = server_socket.accept()
print(f"Conexão recebida de {client_adr}")

# Inicializa o tabuleiro
tabuleiro = init_tab()

# Inicializa o símbolo do jogador
jogador_simbolo = 'X'

while not (check_vitoria(tabuleiro, jogador_simbolo) or check_empate(tabuleiro)):
    # Envia o estado do tabuleiro para o cliente
    tabuleiro_str = "\n".join(" | ".join(linha) for linha in tabuleiro)
    client_socket.send(tabuleiro_str.encode('utf-8'))

    # Aguarda a jogada do jogador
    mov = client_socket.recv(BUFFER_SIZE).decode('utf-8').split(',')
    linha, col = map(int, mov)

    if faz_mov(tabuleiro, linha, col, jogador_simbolo):
        if check_vitoria(tabuleiro, jogador_simbolo):
            print_tabuleiro(tabuleiro)
            client_socket.send("Vitoria".encode('utf-8'))
            break
        elif check_empate(tabuleiro):
            print_tabuleiro(tabuleiro)
            client_socket.send("Empate".encode('utf-8'))
            break

    jogador_simbolo = 'O' if jogador_simbolo == 'X' else 'X'

tabuleiro_str = "\n".join(" | ".join(linha) for linha in tabuleiro)
client_socket.send(tabuleiro_str.encode('utf-8'))

# Fecha a conexão
client_socket.close()
server_socket.close()
