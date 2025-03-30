#Ejercicio 3

contactos = []
N = input("¿Desea agregar un contacto? S para si N para no: ")
while N == "S":
    nombre = input("Ingrese nombre del contacto: ")
    numero = input("Ingrese numero del contacto: ")
    correo = input("Ingrese correo del contacto: ")
    contactos.append(nombre)
    contactos.append((numero, correo))
    N = input("¿Desea seguir agregando contactos? S para si N para no: ")
if N == "N":
    print(contactos)
    N = input("Quiere buscar un contacto? S para si N para no: ")
    if N == "S":
        for i, b in enumerate(contactos):
            print(f"indice {i}: {b}")
        indice = int(input("Escoga el indice de la informacion de su contacto: "))
        print(contactos[indice])