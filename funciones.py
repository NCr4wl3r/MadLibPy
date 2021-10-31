# Funcion cambio genero. Introduce el nombre y adjetivo y los intenta adecuar al genero correcto.
# si el nombre acaba en O o E y el adjetivo acaba en A, le cambia la terminacion a una O.
# Si el nombre acaba en A, y el adjetivo acaba en O, le cambia la terminacion.

def mismoGenero(nom, adj):
    nombre = nom
    adjetivo = adj
    
    # si el nombre es masculino y el adjetivo es femenino(acabado en a)
    if (nombre[-1] == "o") or (nombre[-1] == 'e') and (adjetivo[-1] == 'a'):
        adjetivo = adjetivo.replace(adjetivo[-1], "o")
        print('cambio a o')
    
    # de lo contrario si el nombre es femenino y el adjetivo masculino 
    elif (nombre[-1] == 'a') and (adjetivo[-1] == 'o'):    
        adjetivo = adjetivo.replace(adjetivo[-1], "a")
        print('cambio a a')

    return adjetivo  

def rellenar(nomList, adjList, verbList, hist):
    nombres = nomList
    adjetivos = adjList
    verbos = verbList
    historia = hist

    # loop por toda la historia buscando las marcas <na> y <v> para rellenarla con 
    # los nombres, adjetivos y verbos.
    for palabra in historia:
        if palabra == '<na>':

    
    pass
