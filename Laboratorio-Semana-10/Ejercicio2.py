#Ejercicio 2

dicc = {}
N = str(input("¿Desea agregar un producto?, S para si, N para no: "))
while N == "S":
    nombre = (input("Ingrese nombre del prducto: "))
    cat = (input("Ingrese categoria del producto: "))
    precio = float(input("Ingrese precio del producto: "))
    cantidad = (input("Ingrese cantidad del producto: "))
    dicc[nombre] = {"Categoria":cat, "Precio":precio, "Cantidad":cantidad}
    N = str(input("¿Desea agregar un producto?, S para si, N para no: "))
if N == "N":
    N = (input("Desea eliminar un producto?, S para si, N para no: "))
    if N == "S":
        nombre = input("Ingrese el nombre del producto a eliminar: ")
        del(dicc[nombre])
        print(dicc)
    else:
        buscar = input("Desea buscar un producto? S para si, N para no: ")
        if buscar == "S":
            nombre = input("Nombre del producto: ")
            print(dicc[nombre])
print(dicc)
