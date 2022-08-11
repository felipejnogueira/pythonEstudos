from Funcoes.Users import *
usuarios = {}
opcao = opcoes()

while opcao in ["I", "P", "E", "L"]:
    match opcao:
        case "I":
            inserirUser(usuarios)
        case "P":
            pesquisarUser(usuarios)
        case "E":
            excluirUser(usuarios)
        case "L":
            listarUser(usuarios)

    opcao = opcoes()