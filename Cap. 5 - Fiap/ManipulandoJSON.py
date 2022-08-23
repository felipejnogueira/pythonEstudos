## Importando biblioteca json
import json
from Funcoes.Funcoes import *

def opcoes():
    return int(input("Digite: \n<1> - Para registrar ativo \n<2> - Para salvar \n<3> - Para exibir ativos \n<4> - Para encerrar \n"))

inventario = {}
opcao = opcoes()

while opcao != 4:
    match opcao:
        ## Cadastrar
        case 1:
            registrarPatrimonio(inventario)
        ## Salvar
        case 2:
            salvarJson(inventario)
        ## Exibir
        case 3:
            lerJson()
        ## Encerrar
        case 4:
            break

    opcao = opcoes()
