# Protocolo da Camada de Aplicação

Este documento descreve o protocolo de comunicação utilizado entre o cliente e o servidor no jogo da velha distribuído.

## Evento 1: Conexão Estabelecida

**Descrição:** Este evento ocorre quando o cliente se conecta ao servidor.

**Mensagens:**
- **Servidor para Cliente:** "Conexão estabelecida com sucesso."

## Evento 2: Estado do Tabuleiro Enviado

**Descrição:** Este evento ocorre quando o servidor envia o estado atual do tabuleiro para o cliente.

**Mensagens:**
- **Servidor para Cliente:** Estado atual do tabuleiro representado como uma matriz.

## Evento 3: Jogada do Jogador

**Descrição:** Este evento ocorre quando o cliente faz uma jogada.

**Mensagens:**
- **Cliente para Servidor:** Coordenadas da jogada (linha, coluna).

**Sincronização:**
- O cliente sincroniza seu estado local com o estado atual do tabuleiro recebido do servidor durante o evento "Estado do Tabuleiro Enviado".
- As jogadas do jogador são feitas no estado local do cliente, e essas jogadas são enviadas ao servidor para atualizar o estado global do tabuleiro.

## Evento 4: Resultado da Jogada

**Descrição:** Este evento ocorre quando o servidor processa a jogada do jogador e determina o resultado.

**Mensagens:**
- **Servidor para Cliente:** Resultado da jogada (Vitória, Derrota, Empate).

## Evento 5: Jogo Concluído

**Descrição:** Este evento ocorre quando o jogo é concluído.

**Mensagens:**
- **Servidor para Cliente:** Estado final do tabuleiro após o término do jogo.

## Exemplo de Sequência de Mensagens

1. **Cliente para Servidor:**
   - Evento: Jogada do Jogador
   - Mensagem: "1,2" (representando a jogada na linha 1, coluna 2)

2. **Servidor para Cliente:**
   - Evento: Resultado da Jogada
   - Mensagem: "Vitória" (indicando que o jogador venceu)

3. **Servidor para Cliente:**
   - Evento: Jogo Concluído
   - Mensagem: Estado final do tabuleiro após a vitória.


## Tratamento de Erros

Em caso de eventos incorretos, o sistema apenas encerra o programa. Possíveis causas de erro incluem:
- Recebimento de mensagem invalida.
- Desconexão do cliente.
