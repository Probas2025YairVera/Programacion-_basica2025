#Problema 18

a = int(input('Dame el valor de la variable cuadrada: '))
b = int(input('Dame el valor de la variable lineal: '))
c = int(input('Dame el valor de la constante: '))

if a == 0:
    print('No es de segundo grado')
    exit()
dis = b**2 -4*a*c

if dis >= 0:
    x1 = (-b + dis**0.5)/(2*a)
    x2 = (-b - dis**0.5)/(2*a)
    print(f"X1 = {x1}, X2 = {x2}")
else:
    print('Solucion imaginaria, fuera de mi alcance')