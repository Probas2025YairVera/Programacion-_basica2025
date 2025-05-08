#API DE RICK Y MORTY

import requests


URL = "https://rickandmortyapi.com/api"              #Link principal
URLP = "https://rickandmortyapi.com/api/character"   #Link de los personajes de la serie    
URLE = "https://rickandmortyapi.com/api/episode"     #link de los episodios

respusta = requests.get(URL)
datos = respusta.json()
print(datos)
    
