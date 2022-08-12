with open(input(r"Digite o caminho\nome_arquivo.ext para ler:"), "r") as arq:
    conteudo = arq.readlines()

print("Tipo de dado da variável", type(conteudo))
print("Conteúdo do arquivo:", conteudo)
