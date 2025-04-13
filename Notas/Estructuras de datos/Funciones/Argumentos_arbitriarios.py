#si queremos que un una funcion no tengamos la necesidad de pasar los argumentos justos
#a una funcion, tenemos los argumentos arbitriarios, que son denotados por "*args"

def nombres(*args):
    print("El ultimo es ",args[3], "y el primero es ",args[0])

nombres("Pedro", "Ana", "Carlos", "Francisco") #Ahora no tengo limites de argumentos y puedo poner los que quiera
#El orden de los argumentos empiezan desde 0,1,2,3,...

def suma(*args):
    s = 0
    for arg in args:
        s += arg
    return s

print(suma(1,2,3,4,5,6))