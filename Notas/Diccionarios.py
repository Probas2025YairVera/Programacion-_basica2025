#Diccionarios

#Elementos desordenados, tienen dos elementos por posicion dicc{clave:valor} o {key:value}
#Los diccionarios aceptan cualquier tipo de dato, ya sea entero, flotante, y tambien dentro de los diccionarios puedes poner
#listas, tuplas, u otros diciconarios

#Ejemplo

dicc = {"Azul":"Blue", "Rojo":"Red", "Verde":"Green"}
#Para imprimir un solo elemento de un diccionario se hace
print(dicc["Azul"]) #Tenemos que identificar la clave del valor

#Para agregar elementos a diccionarios
dicc["Amarillo"] = "Yellow" #Asignamos al diccionario la nueva clave y su valor
print(dicc)

#Tambien podemos modificar un elemento
dicc["Azul"]="BLUE" #Para modificar un elemento tenemos que identificar la clave y le asignamos un nuevo valor


#Si queremos eliminar un elemento del diccionario usamos la funcion "del"
del(dicc["Verde"])


