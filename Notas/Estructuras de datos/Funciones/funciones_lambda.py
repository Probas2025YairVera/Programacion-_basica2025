#Funciones lambda

#Son funciones simples y anonimas que se utilizan para realizar operaciones rapidas y pequeñas en expresiones.
#Son utiles en situaciones donde se necesitan funciones temporales o funciones de orden superior.

#SINTAXIS
# lambda parametro: expresion
#Ejemplos
lambda x,y : x + y
                      #Ambas funciones representan lo mismo, pero la lambda son en una sola linea de codigo
def sumar(x,y):
    return x + y

#Las funciones lambda las puedes guardar en una variable para poder llamarla mas sencillo
suma = lambda x,y : x + y
print(suma(5,10))
print(suma(6,8))

#Crear una función anónima que permita conocer si un número es par.

par = lambda x : x%2 == 0
if par(5) == True:
    print('Numero par')
else:
    print('No par')

