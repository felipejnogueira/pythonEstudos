inventario = []
resposta = "S"

while resposta == "S":
    inventario.append(input("Equipamento: "))
    inventario.append(float(input("Valor: ")))
    inventario.append(input("Número de Série: "))
    inventario.append(input("Departamento: "))
    resposta = input("Deseja continuar?").upper()

for item in inventario:
    print(item)
