from funciones import mismoGenero, entradaDatos
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
nombres = entradaDatos(PALABRAS * 2)

print(f"Introduce como minimo {PALABRAS*2} adjetivos para el juego!") 
adjetivos = entradaDatos(PALABRAS * 2)

print(f"Introduce como minimo {PALABRAS} verbos para el juego!:")
verbos = entradaDatos(PALABRAS)

# se carga la historia (extraida desde el archivo historia)
try:
    file = open("historia.txt", 'r')
except:
    print('Error opening "historia" file')

# En el archivo hay dos marcas distintivas en las que se añadiran las palabras:
# <na> aqui ira un nombre + adjetivo con un pronombre determinante al principio
# <v> aqui se introduce un verbo


