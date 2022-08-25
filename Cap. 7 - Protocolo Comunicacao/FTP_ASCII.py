from ftplib import *
import os


def escreverLinha(data):
    arq.write(data)
    arq.write(os.linesep)

ftpAtivo = False
ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())
ftp.login()

arquivo = 'README'
ftp.set_pasv(ftpAtivo)

with open(arquivo, 'w') as arq:
    ftp.retrlines('RETR README', escreverLinha)

ftp.quit()
