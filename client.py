import socket
import os

SERVER_IP = '127.0.0.1'
SERVER_PORT = 5555
BUFFER_SIZE = 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))

try:
    while True:
        # Recebe o estado atual do tabuleiro
        tabuleiro_str = client_socket.recv(BUFFER_SIZE).decode('utf-8')

        # Imprime o tabuleiro
        print(tabuleiro_str)

        while True:
            # Faz a jogada do jogador
            mov = input("Insira a linha e a coluna (separadas por vírgula): ")
            client_socket.send(mov.encode('utf-8'))

            # Recebe o resultado da jogada
            result = client_socket.recv(BUFFER_SIZE).decode('utf-8')
            print(result)

            if result in ["Vitoria", "Derrota", "Empate"]:
                break

except ConnectionAbortedError:
    print("Conexão encerrada pelo servidor.")
finally:
    final_tabuleiro_str = client_socket.recv(BUFFER_SIZE).decode('utf-8')
    print(final_tabuleiro_str)
    client_socket.close()
