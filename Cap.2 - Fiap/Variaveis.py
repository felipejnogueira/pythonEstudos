nome = input("Digite o nome do funcionário: ")
empresa = input("Digite o nome da empresa: ")
qtdeFuncionarios = int(input("Digite a quantidade de funcinários: "))
mediaMensalidade = float(input("Digite a média da mensalidade: "))

print(nome + " trabalha na empresa " + empresa)
print("Possui:", qtdeFuncionarios, "funcionários.")
print("A média da mensalidade é de:", str(mediaMensalidade))


print("==============Verifique os tipos de dados abaixo:==============")
print("O tipo de dado da variavel [nome] é:", type(nome))
print("O tipo de dado da variavel [empresa] é:", type(empresa))
print("O tipo de dado da variavel [qtdeFuncionarios] é:", type(qtdeFuncionarios))
print("O tipo de dado da variavel [mediaMensalidade] é:", type(mediaMensalidade))