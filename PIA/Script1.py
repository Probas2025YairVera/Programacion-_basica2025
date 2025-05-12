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


Per_Male = []       #lista de personajes masculinos
Per_Female = []     #lista de personajes femeninos

for result in datos["results"]:
    if result["gender"] == "Male":
        Per_Male.append(result["name"])
            
   
for result in datos["results"]:
    if result["gender"] == "Female":
         Per_Female.append(result["name"])

#Diccionarios de personajes en base a su especie
Per_Esp = {"Humanos":[], "Aliens":[]}
humanos = []
Aliens = []
for result in datos["results"]:
    if result["species"] == "Human":
        humanos.append(result["name"])
    elif result["species"] == "Alien":
        Aliens.append(result["name"])
print("----PERSONAJES POR SU ESPECIE----")
Per_Esp["Humanos"]=humanos
Per_Esp["Aliens"]=Aliens
print(Per_Esp)

#Diccionario de personajes en base a su estatus
Per_est = {"Vivo":[], "Muerto":[]}
vivo = []
muerto = []

for result in datos["results"]:
    if result["status"] == "Alive":
        vivo.append(result["name"])
    elif result["status"] == "Dead":
        muerto.append(result["name"])
print("----PERSONAJES POR SU ESTATUS----")
Per_est["Vivo"] = vivo
Per_est["Muerto"] = muerto
print(Per_est)


#GUARDAR LOS DATOS EN UN ARCHIVO TXT

with open("Personajestotales.txt", "w") as archivo:
    for personajes in Per_dict:
        archivo.write(personajes + "\n")

with open("Masculinos.txt", "w") as archivo:
    for personajes in Per_Male:
        archivo.write(personajes + "\n")

with open("Femeninos.txt", "w") as archivo:
    for personajes in Per_Female:
        archivo.write(personajes + "\n")

with open("Especie.txt", "w") as archivo:
    for clave,valor in Per_Esp.items():
        archivo.write(f"{clave}: {valor}\n")


with open("Estatus.txt", "w") as archivo:
    for clave,valor in Per_est.items():
        archivo.write(f"{clave}: {valor}\n")