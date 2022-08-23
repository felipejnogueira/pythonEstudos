# Geopy - https://pypi.org/project/geopy/#files
from geopy.geocoders import Nominatim
from Funcoes.Funcoes import lerJson, salvarJson

# Digitação do endereço
rua = input("Digite a rua: ")
numero = input("Digite o número: ")
cidade = input("Digite a cidade: ")
path = input("Digite o caminho para o arquivo do endereço: ")

# Salvando o endereço em um arquivo

# Lista endereço
endereco = {1: [rua, numero, cidade]}
salvarJson(endereco, path)

# Lendo arquivo com endereço
arquivo = lerJson(path)

# Formatando string para pegar coordenadas
localizacao = arquivo["1"]

# Objeto geopy
geolocator = Nominatim(user_agent="wazeyes") #Nome do app

location = geolocator.geocode(localizacao[0] + "," + localizacao[1] + "," + localizacao[2])
saida = {"coordenadas": (location.latitude, location.longitude)}
salvarJson(saida, path+"2")
