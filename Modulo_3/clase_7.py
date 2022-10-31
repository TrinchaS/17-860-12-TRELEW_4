def buscar(lista,valor):
    posicion = 0
    for elemnto in lista:
        if elemento==valor:
            return posicion
        posicion += 1
    return None

def ordenar_seleccion(lista):
    cantidad = len(lista)
    for indice in range(cantidad):
        mini = minimo(lista[indice:cantidad]) #busco el min sobre lo que resta de lista
        if (mini != 0): #!=0 quiere decir que en el indice actual no esta el menor  
            #sumo indice xq es la dif de posiciones entre el que tengo que cambiar y el minimo del resto de la lista
            lista[indice] , lista[mini + indice] = lista[mini + indice] , lista[indice]
    return lista


######## terminar###########
def ordena_insercion(lista):
    for indice in range(len(lista)):
        inserta(elemento,lista[0:indice])

def inserta(elemento,lista):
    if lista:
        
    else:
        return [elemento]
    

    for (indice,elemento) in enumerate(lista):
        if (valor > elemnto):
            x:y:xs
################################


def minimo(lista):
    posicion = 0
    for (indice,elemnto) in enumerate(lista):
        if lista[posicion] > elemnto:
            posicion = indice
    return posicion



rta = ordenar([11,2,4,1,6,8,9])
print(rta)
