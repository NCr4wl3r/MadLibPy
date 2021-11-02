import random

# Funcion cambio genero. Introduce el nombre y adjetivo y los intenta adecuar al genero correcto.
# si el nombre acaba en O o E y el adjetivo acaba en A, le cambia la terminacion a una O.
# Si el nombre acaba en A, y el adjetivo acaba en O, le cambia la terminacion.

def mismoGenero(nom, adj):
    nombre = nom
    adjetivo = adj
    
    # si el nombre es masculino y el adjetivo es femenino(acabado en a)
    if (nombre[-1] == "o") or (nombre[-1] == 'e') and (adjetivo[-1] == 'a'):
        adjetivo = adjetivo.replace(adjetivo[-1], "o")
    
    # de lo contrario si el nombre es femenino y el adjetivo masculino 
    elif (nombre[-1] == 'a') and (adjetivo[-1] == 'o'):    
        adjetivo = adjetivo.replace(adjetivo[-1], "a")

    return adjetivo  

def determinante (palabra):
    if (palabra[-1] == "o") or (palabra[-1] == "e"):
        return "el"
    elif (palabra[-1] == "a"):
        return "la"
    else:
        return "el"

def rellenar(nomList, adjList, verbList, hist):
    nombres = nomList
    adjetivos = adjList
    verbos = verbList
    historia = ""
    
    # shuffle the three list:
    random.shuffle(nombres)
    random.shuffle(adjetivos)
    random.shuffle(verbos)

    # loop por toda la historia buscando las marcas <na> y <v> para rellenarla con 
    # los nombres, adjetivos y verbos.
    for palabra in hist.split():
        if '<na>' in palabra:
            # coge aleatoriamente un nombre y adjetivo
            nombre = nombres.pop(0)
            adjetivo = mismoGenero(nombre, adjetivos.pop(0))
            det = determinante(nombre)
            grupo = det + " " + nombre + " " + adjetivo
            palabra = palabra.replace('<na>', grupo)
        elif '<v>' in palabra:
            palabra = palabra.replace('<v>', verbos.pop(0))
        
        print(palabra)
        historia = historia + palabra + " "
    
    return(historia)

# recoge una lista de palabras con un minimo especificado
def entradaDatos (cantidad):
    palabras = input()
    lstPalabras = palabras.split()
    lenPalabras = len(lstPalabras)
    # si el numero introducido es inferior a la cantidad deseada, se pedira que completen el resto 
    while (lenPalabras < cantidad):
        palabras = ""
        print(f'Faltan {cantidad - lenPalabras}')
        palabras = input()
        for palabra in palabras.split():
            lstPalabras.append(palabra)
        lenPalabras = len(lstPalabras)
    return lstPalabras
