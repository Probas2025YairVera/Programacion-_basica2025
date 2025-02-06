#condiciones
#el for se inicializa dentro de su sintaxis y el while fuera de el

#for control in objetointerable:

#saludos = dict()

#saludos['Español'] = "Hola mundo"
#saludos['English'] = "Hello world"
#saludos['Nihongo'] = "Ohayo"
#saludos['Portugues'] = "saludo al macaco"

#print(saludos.items())

#for idioma,saludo in saludos.items():
    #print(idioma,saludo)

primos = [1,2,3,5,7,11,13,17,19,23,29,31]


setprimos = list()

setprimos.append(num for num in range (0,32) if num in primos)
for num in range (0,31):
    if num in primos:
        print(num)

print(num for num in range (0,32) if num in primos)