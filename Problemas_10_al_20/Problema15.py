#15 Determinar si un año es bisiesto

año = int(input('Indique un año: '))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f'{año} es un año bisiesto')

    
       