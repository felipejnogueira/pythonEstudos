# Importação da lib de socket para comunicação
import socket
from socket import *

# Ip e porta
ip = '127.0.0.1'
porta = 1902

# Objeto de comunicação do socket
objSocket = socket(AF_INET, SOCK_STREAM)
objSocket.bind((ip, porta))
objSocket.listen(2)

print('Aguardando mensagem...')

# Loop infinito escutando mensagens
while True:
    con, client = objSocket.accept()
    while True:
        msgRecebida = str(con.recv(1024))
        print('Recebida:', msgRecebida[2:-1])
        msgEnviada = bytes(input("Enviar: "), 'utf-8')
        con.send(msgEnviada)
        break
    con.close()
