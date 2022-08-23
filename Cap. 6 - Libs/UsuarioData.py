import getpass
from datetime import datetime

print("User:", getpass.getuser())
print("Data Completa:", datetime.now())

print("Dia:", datetime.now().day)
print("Mês:", datetime.now().month)
print("Ano:", datetime.now().year)
print("Hora:", datetime.now().hour)
print("Minuto:", datetime.now().minute)
print("Segundo:", datetime.now().second)

usuario = input("Digite o usuário: ").upper()
senha = getpass.getpass("Digite a senha: ")

if usuario == "FJNOG" and senha == "teste":
    print("Usuário logado!")
else:
    print("Login negado!")
