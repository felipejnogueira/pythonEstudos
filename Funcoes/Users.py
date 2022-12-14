def inserirUser(users):
    users[input("Digite o login do usuário: ").upper()] = [input("Digite o nome do usuário: ").upper(),
                                                   input("Digite a última data de acesso: " ),
                                                   input("Digite a última estação utilizada: ").upper()]
    print("Usuário inserido!")

def pesquisarUser(users):
    login = input("Digite o login para exibir os dados do usuário: ").upper()
    print("Dados: ", users.get(login))

def excluirUser(users):
    chave = input("Digite o login para excluir o usuário: ").upper()
    del users[chave]
    print("Usuário excluído!")

def listarUser(users):
    for chave, valor in users.items():
        print("Usuário:", chave)
        print("Dados:", valor)

def opcoes():
    opcao = input("<I> - Para inserir \n<P> - Para pesquisar \n<E> - Para excluir \n<L> - Para listar usuários \n").upper()
    return opcao
