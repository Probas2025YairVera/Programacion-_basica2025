#Tipos de datos

#Tipos de datos basicos
str()
int()
float()

#Tipos de datos estructurados
list()
dict()
set()
tuple()
#enumerate()
#range()

diasSemana= ['Lun', 'Mar', 'Mier', 'Jue', 'vier']
daysWeek= ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
#print(diasSemana, type(diasSemana), daysWeek, type(daysWeek))

combinado= [5, 3.12, 'gato', diasSemana, 30, daysWeek]
#print(combinado, type(combinado))


#Hay dos formas

#lista = list()
                  #Las dos formas son correctas
#lista = []

#conjunto= set()
#print(type(conjunto))
#conjunto = {1,2,3}        #El diccionario tambien es con {}, pero para diferenciarlo de un set, el set tienen que tener valores dentro
#print(type(conjunto))

conjunto = set()
lista = list()

from random import randint

for i in range(10):
    t = randint(0,100)
    lista.append(t)
    conjunto.add(t)
print(lista)
print(conjunto)

#El set almacena solo una vez el valor

#TUPLA

tupla = tuple()
tupla = ()
