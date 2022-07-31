#Listas
equipamento = []
valor = []
serie = []
departamento = []

continua = "S"

while continua == "S":
    equipamento.append(input("Digite o equipamento: "))
    valor.append(float(input("Digite o valor: ")))
    serie.append(input("Digite o número de série: "))
    departamento.append(input("Digite o departamento: "))
    continua = input("Continua a inserir?").upper()

for indice in range(0,len(equipamento)):
    print("\n Equipamento...: ", indice+1)
    print("\n Nome..........: ", equipamento[indice])
    print("\n Valor.........: ", valor[indice])
    print("\n Serie.........: ", serie[indice])
    print("\n Departamento..: ", departamento[indice])


busca = input("\n Digite o nome de um equipamento para pesquisar: ")

for indice in range(0,len(equipamento)):
    if busca == equipamento[indice]:
        print("\n Nome..........: ", equipamento[indice])
        print("\n Valor.........: ", valor[indice])
        print("\n Serie.........: ", serie[indice])
        print("\n Departamento..: ", departamento[indice])
