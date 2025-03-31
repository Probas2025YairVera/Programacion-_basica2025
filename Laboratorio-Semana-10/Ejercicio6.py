#Sistema de gestion de vehiculos

class vehiculo:
    def __init__(self, marca, modelo, año, precio):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio

marca = input("Marca del coche: ")
modelo = input("Modelo del coche: ")
año = input("Año del coche: ")
precio = input("Precio del coche: ")

A = vehiculo(marca, modelo, año, precio)

sn = input("Desea ver la informacion del vehiculo?\ns para si n para no:  ")
if sn == "s":
    print(A.marca, A.modelo, A.año, A.precio)