#Cual es la complejidad??
#analizamos el peor de los casos

def funcion_confusa_7(a, b):
	if (a < 10):	#1
        return b
	r = 1			#1
	for i in range(a):	#n>=10 veces
		for j in range(b):  #m = b 
			r = r * i * j   #1
	return r 		#1

	#for mas interno --> m veces
	#for mas externo --> n*m veces

	# O(n,m) = 1 + 1+ m*(n * 1) + 1 ==> m=n para simplificar ==> n^2 + 3 ==> n^2


#Ejercicio: Reducir las siguientes complejidades:
# O(17 + n) --> n
# O(79 * n^2) --> n^2
# O(n! + n^20) --> n!
# O(n * log(n) + n^2) --> n^2
# O(n + log(n) + 9) --> n



#Ejercicio: Búsqueda simple
#Cual es la complejidad temporal?
def buscar(vector, elemento):
	index = 0	#1
	for i in vector:	#n
		if (i == elemento):	#1
			return index
		index += 1		#1
	return -1			#1
# O(buscar(n,e)) = n 



#Ejercicio: Ordenamiento trivial
#Cual es la complejidad temporal?

def buscar_maximo(numeros):
	if (len(numeros) < 1):	#1
		return None
	pos = 0					#1
	index = 0				#1
	for candidato in numeros:	#n
		if (candidato > numeros[pos]):	#1
			pos = index		#1
		index += 1			#1
	return pos				#1
	# O(buscar_maximo) = n


def swap(vector, pos1, pos2):
	aux = vector[pos1]			#1
	vector[pos1] = vector[pos2]	#1
	vector[pos2] = aux			#1
	# O(swap) = 3

def ordenar(vector):
	for i in range(len(vector)):	#n
		pos_maximo = buscar_maximo(vector[i:])	#1 + (n-1)
		swap(vector, i, i + pos_maximo)	#3
	return vector
	# O(ordenar) = n*((n-1)+3) = n^2








