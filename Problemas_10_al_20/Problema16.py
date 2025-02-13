#16 Contar el numero de consonantes y vocales de una cadena


def contar(palabra):
    return sum(1 for letra in palabra if letra.lower() in 'aeiou')

palabra = input('Ingrese una palabra: ')
conteos = list(map(contar, palabra))

print(palabra)
print(conteos)