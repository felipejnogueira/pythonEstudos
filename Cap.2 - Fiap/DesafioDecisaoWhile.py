continua = "SIM"

while continua == "SIM":

    nivelAcesso = input("Insira o nível de acesso:").upper()

    if nivelAcesso == "ADM" or nivelAcesso == "USR":
        genero = input("Gênero:").lower()
        if nivelAcesso == "ADM":
            if genero == "feminino":
                print("Olá Administradora!")
            else:
                print("Olá Administrador!")
        else:
            if genero == "feminino":
                print("Olá usuária!")
            else:
                print("Olá usuário!")
    elif nivelAcesso == "GUEST":
        print("Olá visitante!")
    else:
        print("Olá desconhecido(a)")

    continua = input("Digite SIM para continuar... ").upper()
