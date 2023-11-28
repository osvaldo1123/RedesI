# Jogo da Velha - Cliente e Servidor

Este projeto implementa um jogo da velha usando um modelo cliente-servidor. O jogo é baseado em comunicação via sockets TCP.

## Propósito do Software

O propósito do software é capacitar que dois jogadores possam jogar, em um tabuleiro 3x3, uma partida de jogo da velha.

## Motivação da Escolha do Protocolo de Transporte

O protocolo de transporte escolhido é o TCP. Foi escolhido para ter a garantia de que a ordem das mensagens é mantida, o que é essencial para a sincronização do jogo.

## Requisitos Mínimos de Funcionamento

- Python 3.x instalado no sistema.
- Conexão de rede entre o cliente e o servidor.
- Ambos os programas (cliente e servidor) devem ser executados em terminais separados.

## Protocolo da Camada de Aplicação

Para detalhes sobre o protocolo de comunicação, veja o arquivo protocolo.md.

## Instruções de Execução

### Servidor

1. Execute o arquivo `server.py` para iniciar o servidor.
2. Aguarde as conexões dos clientes.

### Cliente

1. Execute o arquivo `client.py`.
2. Siga as instruções na tela para inserir suas jogadas.