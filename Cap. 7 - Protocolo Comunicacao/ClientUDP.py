from socket import *

# Server
server = '127.0.0.1'
port = 43210

# Objeto socket
objSocket = socket(AF_INET, SOCK_DGRAM)
objSocket.connect((server, port))

# Var de controle de encerramento do loop
exit = ''

# Loop para troca de mensagem
while exit != 'X':
    # Mensagem a aenviar
    msg = input('Mensagem: ')

    # Enviando mensagem
    objSocket.sendto(msg.encode(), (server, port))

    # Recebendo resposta
    dados, origem = objSocket.recvfrom(65535)
    print('Resposta:', dados.decode())

    exit = input('Digite <X> para encerrar: ').upper()

objSocket.close()
