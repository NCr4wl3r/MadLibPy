from funciones import mismoGenero
# Madlibpy es un juego en el que se introducen unas palabras (nombres, adjetivos y verbos)
# y se genera una historia aleatoria.
# El juego recogera X nombres, X adejetivos y X verbos.

print("***************************************************************")
print("**      MadLibPY!!        version 0.1      by Espar          **")
print("***************************************************************")
print(" ")
print(" ")
print(" ")

# Primera parte, recogemos los datos, del usuario y del archivo de texto donde estara la historia ('historia')
# Generamos 3 listas: nombres, adejetivos y verbos.

PALABRAS = 10

nombres = []
adjetivos = list()
verbos =[]

print(f"Introduce {PALABRAS} nombres para el juego!") 
nombre = input()
nombres = nombre.split()

print(f"Introduce {PALABRAS} adjetivos para el juego!") 
adjetivo = input()
adjetivos = adjetivo.split()

print(f"Introduce {PALABRAS} verbos para el juego!:")
verbo = input()
verbos = verbo.split()
    
# si el numero de palabras es menor, se reutilizaran las que se han proporcionado, si es mayor se escogeran 
# aleatoriamente 10 de las suministradas.

print(nombres)
print(adjetivos)
print(verbos)

# prueba del cambio de genero:
print (nombres[0])
print (adjetivos[0])

cambio = mismoGenero(nombres[0], adjetivos[0])
print (cambio)
