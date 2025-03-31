#Implementacion de Mergesort

numeros = input("Ingresa una lista de numeros separados por comas: ")

lista = list(map(int,numeros.split(',')))
print(lista)

def mergesort(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izquierda = mergesort(lista[:medio])
    derecha = mergesort(lista[medio:])
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i,j = 0,0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado
lista_ordenada = mergesort(lista)
print("Lista ordenada: ")
print(lista_ordenada)
