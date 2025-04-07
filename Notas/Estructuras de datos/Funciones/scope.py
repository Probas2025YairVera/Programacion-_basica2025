#Scope en programacion se refiere al alcance de las variables
#Por ejemplo, si yo dentro de una funcion defino una variable, una vez dejemos de ejecutar la funcion
#la variable se destruye por lo que solo podemos acceder a ella dentro de la funcion, nunca desde fuera
#Esto se le conoce como VARIABLE LOCAL

#Ejemplo
def funcion():
    variable = 0
    print(variable)
funcion() #Si ejecutamos la funcion se va a imprimir la variable
#print(variable) Pero si queremos imprimirla desde un print y llamamos a la variable nos da error, por que no existe fuera de la funcion

#Pero si hubieramos creado la variable por fuera:

variable = 3
funcion()
print(variable) #Como le dimos un valor a la variable fuera de la funcio se imprime la que esta fuera de ella
#No nos da error o algo solo porque para pyhton son dos variables disitintas aunque tengan el mismo nombre
#Dentro de la funcion tendra preferencia la variable local y fuera de esta la global

#Si dentro de la funcion escrbimos la sentencia "global"
#python asumira que quieres usar la variable con alcance global o sea la variable que esta fuera de la funcion

def funcion():
    global variable
    variable= 0
    print(variable)

funcion()  #Ahora si ejecutamos la funcion o imprimimos la variable, nos dara 0
print(variable)