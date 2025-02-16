#20

#BUSQUEDA BINARIA

lista = [10,5,3,8,7,9,1,2,10,51,32,102]
lista.sort()

#Buscamos el punto medio
#Comprobar si el punto medio es el numero que se busca

def busquedabinaria(valor):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        puntero = (inicio + fin) // 2
        if valor == lista[puntero]:
            return puntero
        elif valor > lista[puntero]:
            inicio = puntero + 1
        else:
            fin == puntero - 1
    return None


def buscarvalor(valor):
    resultado = busquedabinaria(valor)
    if resultado is None:
        return f"El numero {valor} no se encontro"
    else:
        return f"El numero {valor} se encuentra en la posicion {resultado}"

print(buscarvalor(7))