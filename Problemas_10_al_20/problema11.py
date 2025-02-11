#11 Verificar si una cadena es un palindromo
frase = str(input('Ingrese una oracion: '))


def palindromo(frase):
    frase = frase.lower()
    return frase == frase[::-1]
print(palindromo(frase))


