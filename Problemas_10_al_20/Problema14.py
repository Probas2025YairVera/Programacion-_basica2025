#14 Implementar distintos metodos de ordenamiento

#Algoritmos de ordenamiento
'''
lista = [5,7,15,6,84,2,4,1]

longitud = len(lista)

for i in range(longitud - 1):
    menor = i
    for j in range (i + 1, longitud):
        if lista[j] < lista[menor]:
            menor = j
    temporal = lista[menor]
    lista[menor] = lista[i]
    lista[i] = temporal

print(lista)
'''

'''
lista = [5,7,15,6,84,2,4,1]

for i in range(len(lista) - 1):
    for j in range(len(lista) - 1):
        if lista[j] > lista[j + 1]:
            temporal = lista[j]
            lista[j] = lista[j + 1]
            lista[j + 1] = temporal

print(lista)
'''