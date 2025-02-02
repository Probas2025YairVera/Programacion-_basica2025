#4 Generar la secuencia Fibonacci hasta un numero dado de terminos.


def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end="")
        a, b = b, a + b

n = int(input('ingrese un numero: '))
fibonacci(n)
