# Importação de Lib de socket
from socket import *

# Ip e porta do server
ip = '127.0.0.1'
porta = 1902

# Loop p envio de msg
while True:
    # Criando obj de socket
    objSocket = socket(AF_INET, SOCK_STREAM)
    objSocket.connect((ip, porta))

    # Digitando a mensagem
    msgEnviada = bytes(input("Enviar: "), 'utf-8')
    objSocket.send(msgEnviada)

    # Resposta do server
    resposta = str(objSocket.recv(1024))
    print('Recebida:', resposta[2:-1])
    if str(msgEnviada)[2:-1].upper() == 'FIM':
        break;

objSocket.Close()
