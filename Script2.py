
with open("Personajestotales.txt", "r") as archivo:
    contenido = archivo.read()
    Totales=contenido

with open("Masculinos.txt", "r") as archivo:
    Masculinos = archivo.readlines()
   

with open("Femeninos.txt", "r") as archivo:
    Femeninos = archivo.readlines()
    
with open("Humanos.txt", "r") as archivo:
    humanos = archivo.readlines()

with open("Aliens.txt", "r") as archivo:
    aliens = archivo.readlines()


with open("Vivos.txt", "r") as archivo:
    vivos = archivo.readlines() 


with open("Muertos.txt", "r") as archivo:
    muertos = archivo.readlines()


PersonajesH = [Masculino.strip() for Masculino in Masculinos if Masculino.strip()]
cantidad1 = len(PersonajesH)

PersonajesM = [femenina.strip() for femenina in Femeninos if femenina.strip()]
cantidad2 = len(PersonajesM)


dicc1 = {"Hombres" : [cantidad1], "Mujeres" : [cantidad2]}
print(type(dicc1))
print(dicc1)       #Diccionario de personajes masculinos y femeninos

PersonajesHumanos = [humano.strip() for humano in humanos if humano.strip()]
cantidad3 = len(PersonajesHumanos)

PersonajesAliens = [alien.strip() for alien in aliens if alien.strip()]
cantidad4 = len(PersonajesAliens)
dicc2 = {"Humanos" : [cantidad3], "Aliens" : [cantidad4]}
print(dicc2)       #Diccionario de personajes Humanos y Aliens


personajesvivos = [vivo.strip() for vivo in vivos if vivo.strip()]
cantidad5 = len(personajesvivos)

personajesmuertos = [muerto.strip() for muerto in muertos if muerto.strip()]
cantidad6 = len(personajesmuertos)
dicc3 = {"Vivos" : [cantidad5], "Muertos" : [cantidad6]}    
print(dicc3)       #Diccionario de personajes vivos y muertos
