# Import
from geopy.geocoders import Nominatim

# Definição
geolocator = Nominatim(user_agent="wazeyes") #Nome do app

location = geolocator.geocode("228 Silvano de Almeida são Paulo")
print(location.address)
print((location.latitude, location.longitude))
