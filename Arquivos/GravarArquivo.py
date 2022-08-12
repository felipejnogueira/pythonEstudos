#open(camino_arquivo, comando) - w = write / r - read / a - append / x - exclusivo / t - retorna texto (string) / b - retorna binario
with open(input(r"Digite o caminho\nome_arquivo: ")+".txt", "w") as arquivo:
    arquivo.write("Criando um arquivo de teste via python.")
