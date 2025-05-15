import pandas as pd
import matplotlib.pyplot as plt


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


dicc1 = {"Cantidad": ["Personajes"], "Hombres" : [cantidad1], "Mujeres" : [cantidad2]}
print(type(dicc1))
print(dicc1)       #Diccionario de personajes masculinos y femeninos

PersonajesHumanos = [humano.strip() for humano in humanos if humano.strip()]
cantidad3 = len(PersonajesHumanos)

PersonajesAliens = [alien.strip() for alien in aliens if alien.strip()]
cantidad4 = len(PersonajesAliens)
dicc2 = {"Cantidad": ["Personajes"], "Humanos" : [cantidad3], "Aliens" : [cantidad4]}
print(dicc2)       #Diccionario de personajes Humanos y Aliens


personajesvivos = [vivo.strip() for vivo in vivos if vivo.strip()]
cantidad5 = len(personajesvivos)

personajesmuertos = [muerto.strip() for muerto in muertos if muerto.strip()]
cantidad6 = len(personajesmuertos)
dicc3 = {"Cantidad": ["Personajes"], "Vivos" : [cantidad5], "Muertos" : [cantidad6]}    
print(dicc3)       #Diccionario de personajes vivos y muertos


#Hacer el data frame
df = pd.DataFrame(dicc1)
df2 = pd.DataFrame(dicc2)
df3 = pd.DataFrame(dicc3)
df.to_excel("Libro1.xlsx", index=False)
df2.to_excel("Libro2.xlsx",index=False)
df3.to_excel("Libro3.xlsx",index=False)


#GRAFICA1
width = 0.25
workbook1 = "Libro1.xlsx"
DF = pd.read_excel(workbook1)
print(DF.head())
datos = DF[["Cantidad", "Hombres", "Mujeres"]]
datos.plot(x="Cantidad", kind="bar", rot=0)
plt.title("Grafica de personajes por genero")
plt.xlabel("Perosnajes")
plt.ylabel("Cantidad")
plt.grid()
plt.show()

#GRAFICA2

especie = ["Humanos", "Aliens"]
cantidad = [15,5]

plt.pie(cantidad, labels=especie, autopct="%1.1f%%")
plt.title("Grafica de personajes por especie")
plt.show()


#Grafica3

estatus  = ["Vivo","Muerto"]
cantidad = [8,6]

plt.plot(estatus,cantidad,color="blue")
plt.title("Grafica de personajes por estatus")
plt.ylabel("Cantidad")
plt.xlabel("Estatus")
plt.legend()
plt.show()