#Definicion de funciones

#bloque que permite compactar y reutilizar tu codigo
#Puede recibir datos, utilizarlos y devolver datos

#SINTAXIS

def mi_funcion(): #Escribimos "def" seguido del nombre de la funcion y unos parentesis
    print("Hola")          #Dentro de la funcion escribimos el codigo que queramos

#Para usar nuestra funcion o llamar a la funcion solo ponemos el nombre de la funcion y unos parentesis
mi_funcion()

#Ahora si queremos darle datos a la funcion para que los utilice, el argumento ira dentro de los parentesis, el argumento es el dato

def hola(nombre):
    print("hola", nombre)
#Ahora para que esta funcion funcione debemos de mandar a llamar la funcion pero
#ahora le debemos dar el argumento dentro del paretesis
hola("Pyhton")

#Ejemplo 
#Hacer una funcion que nos de el promedio de tres calificaciones

def promedio(num1, num2, num3):
    resultado = num1 + num2 + num3
    resultado = resultado / 3
    return resultado      #El return va acompañado de un valor, ya sea una variable o una expresion
#SI return tambien puede ir acompañado de una expresion entonces podemos simplificar a una linea la funcion

def promedio_2(num1,num2,num3):
    return (num1+num2+num3) / 3


#La diferencia del return y el print
#Print es una funcion de python para imprimir valores por consola y mostrar resultados al usuario que use el codigo
#El return es la sentencia que nos permite utilizar los valores calculados en las funciones

#Podemos a una variable agregarle un valor de acuerdo a una funcion
#Utilizemos el ejemplo anterior

llamada = promedio_2(9,7,8)
print(llamada)