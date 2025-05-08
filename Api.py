#API DE RICK Y MORTY

import requests


URL = "https://rickandmortyapi.com/api"              #Link principal
URLP = "https://rickandmortyapi.com/api/character"   #Link de los personajes de la serie    
URLE = "https://rickandmortyapi.com/api/episode"     #link de los episodios

#PERSONAJES
respusta = requests.get(URLP)
datos = respusta.json()
print("--------PERSONAJES--------")
Per_dict=[]                             #En Per_dict tengo guardados los personajes en forma de lista
for result in datos["results"]:
    Per_dict.append(result["name"])

print(Per_dict)



#EPISODIOS

respuesta2 = requests.get(URLE)
datos2 = respuesta2.json()
print("-------EPISODIOS-------")
for results_ in datos2["results"]:
    print(results_["name"],"-",results_["episode"])

genero = input("----Ingrese el genero de los personajes----\nMale = hombre\nFemale = mujer\n")
Per_Male = []       #lista de personajes masculinos
Per_Female = []     #lista de personajes femeninos
if genero == "Male":
    print("-------PERSONAJES MASCULINOS-------")
    for result in datos["results"]:
        if result["gender"] == "Male":
            Per_Male.append(result["name"])
            
else:
    print("-------PERSONAJES FEMENINOS-------")
    for result in datos["results"]:
        if result["gender"] == "Female":
            Per_Female.append(result["name"])
if genero == "Male":
    print(Per_Male)
else:
    print(Per_Female)


Per_Esp = {"Humanos":[], "Aliens":[]}
for Humano in datos["results"]:
    if result["species"] == "Human":
        Per_Esp["Humanos"].append(result["name"])

print(Per_Esp)
