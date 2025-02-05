num1 = 1
num2 = 2

condicion = num1 >num2
cond = bool(None)
print(condicion, cond)

if condicion:
    print('accion')

if condicion:
    print('verdadero')


if condicion:
    print('accion')
else:
    print('accion')


edad = int(input('pon tu edad'))
cond1= True
while cond1:

    if edad < 18:
        print('eres menor')
    elif edad >= 18 and edad <= 60:
        print('eres adulto')
    elif edad >= 60 and edad <= 99:
        print('saca beca bienestar')
    else:
        print('ya no puedes usar legos')
        if edad == 120:
            cond1 == False



