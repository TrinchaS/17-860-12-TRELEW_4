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

def minimo(lista):
    posicion = 0
    for (indice,elemnto) in enumerate(lista):
        if lista[posicion] > elemnto:
            posicion = indice
    return posicion


# lista[1:] y n+1 porque se supone que el primer elemento esta ordenado
def ordena_insercion(lista):
	for n,l in enumerate(lista[1:]):
		inserta(n+1,lista)

#busca un elemento mayor al lista[indice], si lo encuentra hace el desplazo
def inserta (indice,lista):
	posicion = mayorA(lista[indice],lista[0:indice+1])
	if posicion > -1:
		desplaza(posicion,indice,lista)
	
#retorna la posicion del elemento de la lista mayor a 'e', -1 si no lo encuentra		
def mayorA (e, lista):
	indice = 0 
	for l in lista:
		if l>e:
			return indice
		indice += 1
	return -1

#inicio-fin es la sub-lista que voy a desplazar siempre para la derecha llevando el ultimo elemento al principio
def desplaza(inicio, fin , lista):
	if inicio < fin :
		lista[inicio] , lista[inicio+1:fin+1] = lista[fin] , lista[inicio:fin]


