from socket import *

# Ip do server e porta
servidor = '127.0.0.1'
porta = 43210

# Digitando a mensagem
msg = bytes(input("Digite uma mensagem: "), 'utf-8')

# Criando obj socket
objSocket = socket(AF_INET, SOCK_STREAM)
objSocket.connect((servidor, porta))
objSocket.send(msg)

# Recebe resposta do servidor
answer = objSocket.recv(1024)

print("Recebemos:", answer)
objSocket.close()
