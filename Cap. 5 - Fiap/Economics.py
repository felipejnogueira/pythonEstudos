## variavel para receber caminho do arquivo
path = r'C:\Users\Felipe\Dev\Python\economic-indicators.csv';

total_voos = 0
maior_ano = 0
maior_mes = 0
maior_passageiros = 0
total_passageiros = 0
mes_media = 0
media = 0

## recebe ano a analisar
ano_user = input('Digite o ano a ser analisado: ')

## abre arquivo csv para leitura (r = read)
with open(path, 'r') as boston:
    for linha in boston.readlines()[1:-1]:
        lista = linha.split(",")
        if float(lista[2]) > float(maior_passageiros):
            maior_ano = lista[0]
            maior_mes = lista[1]
            maior_passageiros = lista[2]

        if ano_user == lista[0]:
            total_voos = lista[3]
            total_passageiros = total_passageiros + int(lista[2])
            if float(lista[5]) > float(media):
                media = lista[5]
                mes_media = lista[1]

    print('Mes/Ano com maior trânsito passageiros:', maior_mes + "/" + maior_ano)

    print('------- informações sobre ano analisado -------')
    print('Total de voos:', total_voos)
    print('Total de passageiros no ano:', total_passageiros)
    print('Mes com maior média diaria:', mes_media)

