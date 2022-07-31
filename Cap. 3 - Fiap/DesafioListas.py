#Desafio depreciação

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

#Busca de item para depreciar o valor em 10%
depreciacao = input("Digite o equipamento que receberá depreciação de 10%: ")

for indice in range(0,len(equipamento)):
    if equipamento[indice] == depreciacao:
        print("Valor Antigo: ", valor[indice])
        valor[indice] = valor[indice] * 0.9
        print("Valor Atual: ", valor[indice])

#Busca de item para exclusão das listas
excluir = input("Insira o número de série para excluir o item: ")

for indice in range(0, len(serie)):
    if serie[indice] == excluir:
        del equipamento[indice]
        del valor[indice]
        del serie[indice]
        del departamento[indice]
        print("Equipamento de série:", excluir, "excluído!")
        break


for indice in range(0,len(equipamento)):
    print("\n Equipamento...: ", indice+1)
    print("\n Nome..........: ", equipamento[indice])
    print("\n Valor.........: ", valor[indice])
    print("\n Serie.........: ", serie[indice])
    print("\n Departamento..: ", departamento[indice])
