#Fase II del curso 
#Estructuras de datos

#LISTAS

#Las listas se utilizan con [], y dentro de ellas puedes guardar elementos de tipo entero, decimal, booleanos y cadenas

lista = [29, 2.02, True, "Elemento"] 
#Si queremos imprimir un elemento en especifico de la lista se hace como "print(lista[posicion del elemto])"
print(lista[2])

#Para hacer una sublista podemos hacer "print(lista[posicion elemento:posicion elemento])"
print(lista[1:3])

#Si quieres cambiar el valor de un elemento se hace como lista[posicion del elemento a cambiar] = "nuevo valor asignado"
lista[2] = "Hola"
# O tambien puedes puedes cambiar un elemento por otra lista 
lista[1] = [1,2,3]
print(lista)

#El append se utiliza para agregar un elemento al final
lista.append("si")
#El count nos dice el numero de veces que se repite un elemento
print(lista.count(29))
#El index nos devuelve la posicion de la primera aparicion de un elemento
print(lista.index("Hola"))
#El remove elimina la primera aparicion de un eleme
lista.remove("Hola")
print(lista)