from socket import *

# Server
server = '127.0.0.1'
port = 43210

# Objeto socket UDP - SOCK_DGRAM
objSocket = socket(AF_INET, SOCK_DGRAM)
objSocket.bind((server, port))
print('Server ligado...')

while True:
    dados, origem = objSocket.recvfrom(65535)
    print('Origem:', origem)
    print('Dados recebidos:', dados.decode())
    answer = input('Digite: ')
    objSocket.sendto(answer.encode(), origem)

objSocket.close()
