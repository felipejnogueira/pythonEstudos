## Importando biblioteca json
import os, json
from Funcoes.Funcoes import *

def opcoes():
    return int(input("Digite: \n<1> - Para registrar ativo \n<2> - Para salvar \n<3> - Para exibir ativos \n<4> - Para encerrar \n"))


# Pegando caminho do arquivo
path = input(r"Digite o caminho\nome_arquivo.ext para ler")

# Carregando arquivo na variavel de inventario
with open(path, "r") as arquivo:
    if os.path.exists(path):
        inventario = json.load("path")
    else:
        inventario = {}

# Menu de opções
opcao = opcoes()
while opcao != 4:
    match opcao:
        # Cadastrar
        case 1:
            registrarPatrimonio(inventario)
        # Salvar
        case 2:
            salvarJson(inventario, path)
        # Exibir
        case 3:
            lerJson()
        # Encerrar
        case 4:
            break

    opcao = opcoes()
