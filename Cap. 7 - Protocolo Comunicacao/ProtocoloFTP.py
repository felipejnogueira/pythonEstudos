# Import da lib de ftp
from ftplib import *

# Conexão passiva de FTP
ftpAtivo = False

# Servidor FTP
ftp = FTP('ftp.ibge.gov.br')

# Mensagem padrão do servidor
print(ftp.getwelcome())

# User / Senha
user = input('Digite o usuario: ')
password = input('Digite a senha: ')

# Login no server ftp
ftp.login(user, password)

# Loop de navegação
while exit != 'X':
    # Lista diretorios
    print(ftp.dir())
    pasta = input('Digite a pasta para navegar: ')

    # Troca de pasta dentro do FTP
    ftp.cwd(pasta)

    # Encerra navegação
    exit = input('Digite <X> para encerrar navegação: ')

#print('Diretorio atual:', ftp.pwd())

#print(ftp.retrlines('LIST'))

# fechamento da conexão
ftp.quit()
