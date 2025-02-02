#6 Calcular el interes compuesto dado un capital, tasa y tiempo

A = float(input('Dinero invertido: '))
B = float(input('Compra anual: '))
C = int(input('Años de inversion: '))
D = float(input('Interes ganado anualmente: '))

result = A
for i in range(C):
    result = result + B
    result = result + (D * result / 100)

print(result)

 
