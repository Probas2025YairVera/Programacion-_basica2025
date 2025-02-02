#2 Crear un calculadora simple que realice operaciones basicas

A = float(input('Ingrese un numero: '))
B = float(input('Ingrese otro numero: '))

Op = str(input('seleccione una operacion + - * /: '))

while B == 0:
    B = float(input('Ingrese un numero diferente de 0: '))

if Op == '+':
    print( A + B)
elif Op == '-':
    print(A - B)
elif Op == '*':
    print(A * B)
else:
    print(A / B)

   