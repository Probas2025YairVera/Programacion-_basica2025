#API DE RICK Y MORTY

import requests


URL = "https://rickandmortyapi.com/api"              #Link principal
URLP = "https://rickandmortyapi.com/api/character"   #Link de los personajes de la serie    
URLE = "https://rickandmortyapi.com/api/episode"     #link de los episodios

#PERSONAJES
respusta = requests.get(URLP)
datos = respusta.json()
print("--------PERSONAJES--------")
for result in datos["results"]:
    print(result["name"])



#EPISODIOS

respuesta2 = requests.get(URLE)
datos2 = respuesta2.json()
print("-------EPISODIOS-------")
for results_ in datos2["results"]:
    print(results_["name"],"-",results_["air_date"])


genero = input("Ingrese el genero de los personajes\nMale = hombre\nFemale = mujer\n")

if genero == "Male":
    print("-------PERSONAJES MASCULINOS-------")
    for result in datos["results"]:
        if result["gender"] == "Male":
            print(result["name"])
else:
    print("-------PERSONAJES FEMENINOS-------")
    for result in datos["results"]:
        if result["gender"] == "Female":
            print(result["name"])

        

