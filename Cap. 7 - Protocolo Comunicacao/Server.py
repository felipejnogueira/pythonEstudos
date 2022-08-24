from socket import *

# Ip do server e porta
server = '127.0.0.1'
port = 43210

# Objeto de comunicação
objSocket = socket(AF_INET, SOCK_STREAM)   #AF_INET - DNS | SOCK_STREAM - TCP / SOCK_DGRAM - UDP
objSocket.bind((server, port))
objSocket.listen(2)    # Quantidade de clients conectados simultaneamente

print("Aguardando client...")

# Loop infinito para checar chamadas
while True:
    con, client = objSocket.accept()   # Aguardando conexão do client
    print("Conectado com:", client)
    while True:
        msgReceived = str(con.recv(1024))   # 1024 bytes
        print("Recebemos:", msgReceived)
        msgSent = b"Ola cliente" # b - bytes | Socket se comunica apenas em bytes
        con.send(msgSent)
        break
    con.close()
