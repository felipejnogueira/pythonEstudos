from ftplib import *


# from Funcoes.ftpFunctions import *


# Função para exibir e retornar opções
def opcoes():
    return input('Selecione: \n1 - Selecionar servidor ftp \n2 - Navegar no servidor \n'
                 '3 - Baixar arquivo \n4 - Encerrar sistema\n')


# Variaveis necessarias
opc = 0
objFTP = FTP('')

# Enquanto não encerrar
while opc != 4:
    opc = int(opcoes())
    match opc:
        case 1:
            ip = input('Digite a url do servidor ftp: ')
            # Cria obj ftp
            objFTP = FTP(ip)

            # User/Senha
            user = input('Login: ')
            password = input('Senha: ')

            # Login no server ftp
            objFTP.login(user, password)
        case 2:
            objFTP.dir()
            print(objFTP.dir())
            directory = input('Digite a pasta para navegar: ')
            objFTP.cwd(directory)

            print('Diretório atual:', objFTP.pwd())
        case 3:
            print(objFTP.dir())
            file = input('Digite o nome do arquivo para download: ')

            with open(file, 'wb') as arq:
                objFTP.retrbinary('RETR ' + file, arq.write)
        case 4:
            objFTP.close()
            print('Sistema encerrado!')
            break
        case other:
            print('Opção não encontrada!')
