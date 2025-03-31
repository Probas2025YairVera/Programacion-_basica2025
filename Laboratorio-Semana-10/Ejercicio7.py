#Ordenamineto y busqueda

import random 

n = int(input("Cantidad de numeros de lista: "))
inicio = 1
fin = int(input("Limite del valor para los numeros de lista: "))

lista = [random.randint(inicio,fin) for i in range(n)]
print(lista)

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]
    return quicksort(menores) + iguales + quicksort(mayores)

print("Lista ordenada: ")
print(quicksort(lista))

    