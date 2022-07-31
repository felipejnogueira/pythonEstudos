def preencherInventario(lista):
    resp = "S"

    while resp == "S":
        equipamento = [
            input("Equipamento: "),
            float(input("Valor: ")),
            int(input("Número de Série: ")),
            input("Departamento: ")
        ]
        lista.append(equipamento)
        resp = input("Deseja continuar a inserir? (S - Sim / N - Não) ")

def exibirElemento(elemento):
    print("Nome.........: ", elemento[0])
    print("Valor........: ", elemento[1])
    print("Série........: ", elemento[2])
    print("Departamento.: ", elemento[3])  

def exibirInventario(lista):
    for elemento in lista:
        exibirElemento(elemento)

def pesquisarNome(lista):
    nome = input("Digite o nome a ser procurado: ")
    for elemento in lista:
        if elemento[0] == nome:
            exibirElemento(elemento)

def depreciarNome(lista):
    nome = input("Digite o nome a ser depreciado: ")
    for elemento in lista:
        if elemento[0] == nome:
            print("Nome: ", elemento[0])
            print("Valor Antigo: ", elemento[1])
            elemento[1] = elemento[1] * 0.9
            print("Valor Novo: ", elemento[1])

def excluirSerie(lista):
    serie = input("Digite o número de sério do equipamento a ser excluído: ")
    for elemento in lista:
        if elemento[2] == serie:
            lista.remove(elemento)

def resumirValores(lista):
    valores = []
    for elementos in lista:
        valores.append(elemento[1])
    
    if len(valores) > 0:
        print("O equipamento mais caro custa R$", max(valores))
        print("O equipamento mais baratto custa R$", min(valores))
        print("O valor total dos equipamentos é de R$", sum(valores))

