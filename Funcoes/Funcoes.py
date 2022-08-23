import json


def preencherInventario(lista):
    resp = "S"

    while resp == "S":
        equipamento = [
            input("Equipamento: "),
            float(input("Valor: ")),
            input("Número de Série: "),
            input("Departamento: ")
        ]
        lista.append(equipamento)
        resp = input("Deseja continuar a inserir? (S - Sim / N - Não) ").upper()


def exibirElemento(elemento):
    print("Nome:", elemento[0], "Valor: R$", elemento[1], "Série:", elemento[2], "Departamento:", elemento[3])


def exibirInventario(lista):
    for elemento in lista:
        exibirElemento(elemento)


def pesquisarNome(lista):
    nome = input("Digite o nome a ser procurado: ")
    for elemento in lista:
        if elemento[0] == nome:
            exibirElemento(elemento)


def depreciarNome(lista, porc):
    nome = input("Digite o nome a ser depreciado: ")
    for elemento in lista:
        if elemento[0] == nome:
            print("Nome: ", elemento[0])
            print("Valor Antigo: ", elemento[1])
            elemento[1] = elemento[1] - (elemento[1] * (porc/100))
            print("Valor Novo: ", elemento[1])


def excluirSerie(lista):
    serie = input("Digite o número de sério do equipamento a ser excluído: ")
    for elemento in lista:
        if elemento[2] == serie:
            lista.remove(elemento)
    return "Item excluído!"


def resumirValores(lista):
    valores = []
    for elemento in lista:
        valores.append(elemento[1])
    
    if len(valores) > 0:
        print("O equipamento mais caro custa R$", max(valores))
        print("O equipamento mais barato custa R$", min(valores))
        print("O valor total dos equipamentos é de R$", sum(valores))


def registrarPatrimonio(inventario):
    resp = "S"
    while resp == "S":
        inventario[input("Digite o número patrimonial: ")] = [input("Digite a data da última atualização: "),
                                                              input("Digite a descrição: "),
                                                              input("Digite o departamento: ")]
        resp = input("Digite <S> para continuar: ").upper()


def salvarArquivo(inventario):
    with open(input(r"Digite o Caminho\nome_arquivo para salvar:")+".csv", "a") as arq:
        for chave, valor in inventario.items():
            arq.write(chave + ";" + valor[0] + ";" + valor[1] + ";" + valor[2] + ";\n")
        print("Arquivo salvo!")


def lerArquivo():
    with open(input(r"Digite o caminho\nome_arquivo.ext para ler"), "r") as arq:
        return arq.readlines()


def salvarJson(inventario, path):
    with open(input(r"Digite o Caminho\nome_arquivo para salvar:")+".json","w") as arq:
        json.dump(inventario, arq)
    print("Arquivo salvo!")


def lerJson(path):
    with open(path, "r") as arq:
        resultado = json.load(arq)
        for chave, dado in resultado.items():
            print("Data:", dado[0])
            print("Descrição:", dado[1])
            print("Departamento:", dado[2])
