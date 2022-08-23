inventario = []
continua = "S"

while continua == "S":
    equipamento = [
        input("Equipamento: "),
        float(input("Valor: ")),
        int(input("Número de Série: ")),
        input("Departamento: ")
    ]
    inventario.append(equipamento)
    continua = input("Deseja continuar a inserir? (S - Sim / N - Não) ")

for elemento in inventario:
    print("Nome.........: ", elemento[0])
    print("Valor........: ", elemento[1])
    print("Série........: ", elemento[2])
    print("Departamento.: ", elemento[3])

busca = input("Digite o nome do equipamento que deseja buscar: ")

for elemento in inventario:
    if equipamento[0] == busca:
        print("Nome.........: ", elemento[0])
        print("Valor........: ", elemento[1])
        print("Série........: ", elemento[2])
        print("Departamento.: ", elemento[3])

serial = int(input("Digite o número de série do equipamento para excluir: "))
for elemento in inventario:
    if elemento[2] == serial:
        inventario.remove(elemento)

for elemento in inventario:
    print("Nome.........: ", elemento[0])
    print("Valor........: ", elemento[1])
    print("Série........: ", elemento[2])
    print("Departamento.: ", elemento[3])

valores = []
for elemento in inventario:
    valores.append(elemento[1])

if len(valores) > 0:
    print("O equipamento mais caro custa: R$", max(valores))
    print("O equipamento mais barato custa: R$", min(valores))
    print("O valor total dos equipamentos é: R$", sum(valores))
