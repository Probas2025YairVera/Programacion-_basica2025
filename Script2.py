with open("Personajestotales.txt", "r") as archivo:
    contenido = archivo.read()
    Totales=contenido

with open("Masculinos.txt", "r") as archivo:
    contenido = archivo.read()
    Masculinos = contenido

with open("Femeninos.txt", "r") as archivo:
    contenido = archivo.read()
    Femeninos = contenido

with open("Estatus.txt", "r") as archivo:
    contenido = archivo.read()
    Estatus = contenido

with open("Especie.txt", "r") as archivo:
    contenido = archivo.read()
    Especie = contenido

print(Totales)



