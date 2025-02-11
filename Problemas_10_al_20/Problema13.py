#13 Convertir una temepratura entre distintas escalas

temp = float(input('Ingrese la temperatura: '))
escala = int(input('Indique el numero de cada escala Fahrenheit(1), Celsius(2) o Kelvin(3): '))

if escala == 1:
    print(f'Temperatura en Fahrenheit = {temp}')
    tempc= (temp - 32) * 0.5556
    tempk = (temp - 32)/1.8 + 273.15
    print(f'Temperatura en Celcius = {tempc}\nTemperatura en Kelvin = {tempk}')
elif escala == 2:
    tempf = (temp * 9 / 5 + 32)
    tempk = temp + 273.15
    print(f'Temperatura en Celsius = {temp}\nTemperatura en Fahrenheit = {tempf}\nTemperatura en Kelvin = {tempk}')
else:
    tempf = (temp - 273.15) * 1.8 + 32
    tempc = temp - 273.15
    print(f'Temperatura en Kelvin = {temp}\nTemperatura en Fahrenheit = {tempf}\nTemperatura en Celsius = {tempc}')


    

