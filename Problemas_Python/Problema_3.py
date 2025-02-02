
#3 Calcular el factorial de un numero dado

num = int(input('intoduzca un numero: '))

def factorial(num):
    if num == 0 or num == 1:
        resultado = 1
    elif num > 1:
        resultado = num * factorial(num - 1)
    return resultado







 