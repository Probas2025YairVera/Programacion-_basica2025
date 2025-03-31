#Modulos deconversion de unidades

sn = input("a si quiere convertir kilometros a millas\n"
"b si quieres convertir celsius a fahrenheit\n"
"c si quieres convertir litros a galones\n")

if sn == "a":
    a = float(input("kilometros a convertir: "))
    from conversor import kilometros_millas
    kilometros_millas(a)
elif sn == "b":
    a = float(input("Grados celsius a convertir: "))
    from conversor import celsius_fah
    celsius_fah(a)
else:
    a = float(input("Litros a convertir: "))
    from conversor  import litros_galones
    litros_galones(a)

