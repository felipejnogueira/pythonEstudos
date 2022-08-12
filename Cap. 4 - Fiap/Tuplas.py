ips = {}
resp = "S"

while resp == "S":
    ips[(input("Digite os dois primeiros octetos do ip: "), input("Digite os dois ultimos octestos do ip: "))] = input("Nome da máquina: ")

    resp = input("Digite <S> para continuar: ").upper()

print("Exibindo ip's: ")
for ip in ips.keys():
    print(ip[0]+"."+ip[1])

print("Exibindo máquina com o mesmo endereço: ")
pesq = input("Digite os dois ultimos octetos: ")

print("Máquinas no mesmo endereço (redes diferentes)")
for ip,nome in ips.items():
    if(ip[1] == pesq):
        print(nome)

print("Máquinas na mesma rede: ")
pesq = input("Digite os dois primeiros octetos: ")
for ip,nome in ips.items():
    if(ip[0] == pesq):
        print(nome)
