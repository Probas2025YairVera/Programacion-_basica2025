#TUPLAS
# secuencia ordenada, Heterogenea y NO SE PUEDE MODIFICAR
#Al igual que las listas podemos guardar cualquier tipo de elementos
#Las tuplas se hacen con ()
#Las tuplas solo ofrecen el count y el metodo index

from googletrans import Translator

translator = Translator()

texto = "hello world"
result = translator.translate(texto, dest="fr")
print(result,texto)