import socket

# Recebe url
url = input("Digite uma url: ")

# Pega ip da url
ip = socket.gethostbyname(url)

print("O ip da url é:", ip)

# Exibindo portas para os protocolos
print("Porta Dominio:", socket.getservbyname("domain"))
print("Porta HTTP:", socket.getservbyname("http"))
print("Porta FTP", socket.getservbyname("ftp"))
