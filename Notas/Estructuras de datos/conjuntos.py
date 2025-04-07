#CONJUNTOS
#Los conjuntos son una coleccion de elementos no ordenados
#Heterogeneos pero solo con elementos inmutables
#Mutables y sin repeticion 
#Para declarar un conjunto se usan {}, pero como el diccionario tambien las usa, usaremos "set"
'''
print(set([1, 2 ,3 , 4]))
print(set((5, 2, 4.12, 4)))
print(set("1524"))
'''
#Uno de sus usos es eliminar elementos repetidos de la secuencia
conjunto = set([2,4,5,2])
print(conjunto)

#Podemos añadir un elemento con add
conjunto.add(0)
print(conjunto)
#O eliminarlo con remove
conjunto.remove(5)
print(conjunto)

#Tambien podemos crear operaciones de conjuntos

conjunto_1 = set([1, 2, 3, 4])
conjunto_2 = set([5, 3, 2, 5])
print(conjunto, conjunto_1, conjunto_2)
#Podemos hacer una interseccion con "intersection" que devuelve los elementos que aparecen en ambos conjuntos
print(conjunto.intersection(conjunto_1))

#O con la funcion "issubset" podemos comprobar si los elementos de un conjunto estan incluidos en otro

print(conjunto_1.issubset(conjunto_2))

#Algunos operadores que se pueden usar son "A|B" = UNION, "A-B"= DIFERENCIA, "A>=B" = superconjunto
# A&B = INTERSECCION, A^B= DIFERENCIA SIMETRICA, A<=B = SUBCONJUNTO

print(conjunto|conjunto_1)
print(conjunto-conjunto_2)
print(conjunto&conjunto_1)
