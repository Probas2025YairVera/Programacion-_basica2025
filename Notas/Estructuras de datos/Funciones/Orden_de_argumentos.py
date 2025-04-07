#ejemplo de que importa el orden de los argumentos

def resta(num1,num2):
    return num1 - num2

print(resta(5,3))
print(resta(3,5))

#Hay una forma de especificar el orden y son con los "Keyword argument"
#los keyword argument son los nombres que les has dado a tus argumentos
#Con el ejemplo anterior vimos que si ponemos los argumentos (5,3) el resultado es dos, pero si cambiamos eso por:

print(resta(num2 = 5, num1 = 3))
#Ahora nos da -2, esto es porque nosotros hemos asignado que valor queremos en cada argumeto

#Ahora tenemos unos ejemplos
def resta_2(num1 = 3, num2= 2):
    return num1 - num2

print("con valores por defecto:", resta_2())
print("Usando el orden con solo 1 valor:", resta_2(5))
print("Usandoel orden con todos los valores:", resta_2(5,3))
print("Con keyword arguments:", resta_2(num1=5, num2=3))
print("Con solo un keyword argument:", resta_2(num2=3))