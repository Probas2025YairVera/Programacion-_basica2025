#12 Encontrar el mayor entre 3 numeros dados
A = int(input('Ingrese un numero: '))
B = int(input('Ingrese un segundo numero: '))
C = int(input('Ingrese un ultimo numero: '))

if A > B and A > C:
    print(f'{A} es mayor')
elif B > A and B > C:
    print(f'{B} es mayor')
else:
    print(f'{C} es mayor')

