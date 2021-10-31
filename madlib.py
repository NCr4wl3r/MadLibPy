from funciones import mismoGenero
# Madlibpy es un juego en el que se introducen unas palabras (nombres, adjetivos y verbos)
# y se genera una historia aleatoria.
# El juego recogera X nombres, X adjetivos y X verbos.

print("***************************************************************")
print("**      MadLibPY!!        version 0.1      by Espar          **")
print("***************************************************************")
print(" ")
print(" ")
print(" ")

# Primera parte, recogemos los datos, del usuario y del archivo de texto donde estara la historia ('historia')
# Generamos 3 listas: nombres, adejetivos y verbos.

PALABRAS = 5

nombres = []
adjetivos = list()
verbos =[]

# se recoge las palabras y se guardan en listas
print(f"Introduce como minimo {PALABRAS*2} nombres para el juego!") 
nombre = input()
nombres = nombre.split()
lenNom = len(nombres)
# si el numero de palabras es menor, se pediran que se completen las que faltan:
while (lenNom < PALABRAS*2):
    nombre = ""
    print(f"Faltan {PALABRAS*2 -lenNom} nombres")
    nombre = input()
    for palabra in nombre.split():
        nombres.append(palabra)
    lenNom = len(nombres)
print(nombres)

print(f"Introduce como minimo {PALABRAS*2} adjetivos para el juego!") 
adjetivo = input()
adjetivos = adjetivo.split()
lenAdj = len(adjetivos)

while (lenAdj < PALABRAS*2):
    adjetivo = ""
    print(f"Faltan {PALABRAS*2 -lenAdj} adjetivos")
    adjetivo = input()
    for palabra in adjetivo.split():
        adjetivos.append(palabra)
    lenAdj = len(adjetivos)
print(adjetivos)

print(f"Introduce como minimo {PALABRAS} verbos para el juego!:")
verbo = input()
verbos = verbo.split()
lenVerb = len(verbos)
   
while (lenVerb < PALABRAS):
    verbo = ""
    print(f"Faltan {PALABRAS*2 -lenVerb} verbos")
    verbo = input()
    for palabra in verbo.split():
        verbos.append(palabra)
    lenVerb = len(verbos)
print(verbos)

# se carga la historia (extraida desde el archivo historia)
try:
    file = open("historia.txt", 'r')
except:
    print('Error opening "historia" file')

# En el archivo hay dos marcas distintivas en las que se añadiran las palabras:
# <na> aqui ira un nombre + adjetivo con un pronombre determinante al principio
# <v> aqui se introduce un verbo


