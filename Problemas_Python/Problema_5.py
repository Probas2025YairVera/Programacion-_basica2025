#5 Verificar si un numero es primo

num = int(input('ingrese un numero: '))
primo = True

for n in range(2,num):
    if num % n == 0:
        print('No es primo', n, 'es divisor')
        primo = False
        break
if primo:
    print('Es primo')
