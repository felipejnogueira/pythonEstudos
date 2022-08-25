from ftplib import *

# Função para conectar no server FTP
def ftpConnect(objFTP, ipServer):
    # Cria obj ftp
    objFTP = FTP(ipServer)

    # User/Senha
    user = input('Login: ')
    password = input('Senha: ')

    # Login no server ftp
    objFTP.login(user, password)


# Função para navegar no server FTP
def ftpBrowse(objFTP):
    objFTP.dir()
    print(objFTP.dir())
    directory = input('Digite a pasta para navegar: ')
    objFTP.cwd(directory)

    print('Diretório atual:', objFTP.pwd)


# Função para baixar arquivo
def ftpDownload(objFtp):
    print(objFtp.dir())
    file = input('Digite o nome do arquivo para download: ')

    with open(file, 'wb') as arq:
        objFtp.retrbinary('RETR', file, arq.write)
