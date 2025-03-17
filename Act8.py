

palabra = input("Palabra: ")
palabra = palabra.lower()

def contadorDeVocales():
    dicc = {"a": 0, "e": 0, "i": 0, "o": 0, "u":0}
    for letra in palabra:
        if letra in "a":
            dicc["a"] += 1
        elif letra in "e":
            dicc["e"] += 1
        elif letra in "i":
            dicc["i"] += 1
        elif letra in "o":
            dicc["o"] += 1
        elif letra in "u":
            dicc["u"] += 1
    for clave, valor in dicc.items():
        print(clave, valor)


contadorDeVocales()
