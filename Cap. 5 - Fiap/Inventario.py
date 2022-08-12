from Funcoes.Funcoes import *

def opcoes():
    return int(input("Digite: \n<1> - Para registrar ativo \n<2> - Para salvar \n<3> - Para exibir ativos \n<4> - Para encerrar \n"))

inventario = {}
opcao = opcoes()

while opcao != 4:
    match opcao:
        case 1:
            registrarPatrimonio(inventario)
        case 2:
            salvarArquivo(inventario)
        case 3:
            linhas = lerArquivo()
            for linha in linhas:
                print(linha)
        case 4:
            break

    opcao = opcoes()
