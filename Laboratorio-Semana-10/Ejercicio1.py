#Analisis de texto con diccionarios y conjuntos

texto = str(input("Ingrese un texto: "))

def contar(texto):
    palabras = texto.split()
    return len(palabras)
total = contar(texto)

def texto_a_conjunto(texto):
    palabras = set(texto.split())
    return palabras
conjunto = texto_a_conjunto(texto)

def texto_a_dict(texto):
    palabras = texto.lower().split()
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    palabra_frecuente = max(frecuencia, key=frecuencia.get)
    max_frecuencia= frecuencia[palabra_frecuente]
    return frecuencia, palabra_frecuente, max_frecuencia

frecuencia_palabras, palabra_frecuente, veces = texto_a_dict(texto)

print(f"El total de palabras son {total}")
print(f"El total de palabras unicas son {len(conjunto)}")
print(f"La palabra mas frecuente es {palabra_frecuente} y aparece {veces} veces")