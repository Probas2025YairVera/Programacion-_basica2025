#Ejercicio 4

numeros = input("Ingresa una lista de numeros separados por comas: ")

lista = list(map(int,numeros.split(',')))

promedio = lambda *args: sum(args) / len(args) if args else 0
print("El promedio es:", promedio(*lista))
