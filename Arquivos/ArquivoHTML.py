with open(r"C:\Users\Felipe\Dev\Python\pagina.html", "w") as pagina:
    pagina.write("<body> <h1> Teste de página WEB </h1>")
    pagina.write("<br><h2> Abaixo seguem alguns nomes importantes para o projeto: </h2>")
    pagina.write("<h3>")

    nome = ""
    while nome != "SAIR":
        nome = input("Digite um nome ou SAIR: ").upper()
        if nome != "SAIR":
            pagina.write("<br>"+nome)
    pagina.write("</h3></body>")
