def listas_para_llenar_posiciones(int n): ###Recibe el número de partículas y crea una lista con sublistas.
    cdef int j 
    lista_principal = []   ###Cada partícula tiene una lista que ocupa una posicion en lista_principal
    for j in range(n):     ###y a su vez estas listas tienen dos listas para almacenar la información 
        lista_principal.append([[],[]]) ###de la posición en x y y de esa partícula.
    return lista_principal

def listas_para_llenar_componentes_velocidad(int n):
    cdef int j
    lista_principal = []   ###Cada partícula tiene una lista que ocupa una posicion en lista_principal
    for j in range(n):     ###y a su vez estas listas tienen dos listas para almacenar la información 
        lista_principal.append([[],[]]) ###de la velocidad en x y y de esa partícula.
    return lista_principal 