from Funcoes.Funcoes import *

#Declaração de variaveis
minhaLista = []
opcao = 9

while opcao != 0:
    opcao = int(input("Escolha uma opção.\n"
                      "1 - Inserir Equipamentos\n"
                      "2 - Exibir Inventário\n"
                      "3 - Pesquisar Equipamento\n"
                      "4 - Depreciar Valor\n"
                      "5 - Excluir Item\n"
                      "6 - Resumo de Valores\n"
                      "0 - Encerrar\n"))

    match opcao:
        case 1:
            preencherInventario(minhaLista)
        case 2:
            exibirInventario(minhaLista)
        case 3:
            pesquisarNome(minhaLista)
        case 4:
            perc = int(input("Insira a % de depreciação no valor do item:"))
            depreciarNome(minhaLista, perc)
        case 5:
            excluirSerie(minhaLista)
        case 6:
            resumirValores(minhaLista)
        case 0:
            break