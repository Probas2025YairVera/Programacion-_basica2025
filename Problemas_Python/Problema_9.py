#9 Generar una lista de numeros pares e impares hasta un limite dado

lim = int(input('ingrese el limite: '))
listp = []
listi = []

for i in range(1, lim + 1):
    if i%2 == 0:
        listp.append(i)
    else:
        listi.append(i)

impresion = max(len(listp), len(listi))
for j in range(impresion):
    print(listp[j], listi[j])
    



