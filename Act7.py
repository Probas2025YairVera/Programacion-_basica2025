a = int(input('Ingrese valor de la variable cuadratica: '))
b = int(input('Ingrese valor de la vairiable lineal: '))
c = int(input('Ingrese valor de la constante: '))

def discriminante():
    dis = b**2 - 4*a*c
    if dis > 0:
        x1 = (-b + dis**(1/2))/(2*a)
        x2 = (-b - dis**(1/2))/(2*a)
        print(f"{x1} y {x2}")
    elif dis == 0:
        x1 = (-b + dis**(1/2)) / (2*a)
        print(x1)
    else:
        dis = dis * -1
        x1 = (-b + dis**(1/2))/(2*a)
        x2 = (-b - dis**(1/2))/(2*a)
        print(f"{x1}i y {x2}i")

discriminante()




