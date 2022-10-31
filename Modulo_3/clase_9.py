def fibonacci(n):
	if n <= 1:
		return 1
	return fibonacci(n-2) + fibonacci(n-1)


def busqueda_binaria(arreglo, inicio, fin, n):
	if inicio > fin:
		return -1
	medio = (inicio + fin) // 2
	if (arreglo[medio] == n):
		return medio
	if (arreglo[medio] < n):
		return busqueda_binaria(arreglo, medio + 1, fin, n)
	else:
		return busqueda_binaria(arreglo, inicio, medio - 1, n)


# O(n*log(n))
def mergesort(arreglo):
	largo = len(arreglo)
	if largo <= 1:
		return arreglo
	medio = largo // 2
	primera_mitad = arreglo[0:medio]
	segunda_mitad = arreglo[medio:largo]
	primera_mitad_ordenada = mergesort(primera_mitad)
	segunda_mitad_ordenada = mergesort(segunda_mitad)
	return merge(primera_mitad_ordenada, segunda_mitad_ordenada)

def merge(left, right):
	result = []
	i, j = 0, 0
	while i < len(left) and j < len(right):
		if left[i] <= right[j] :
			result.append(left[i])
			i = i + 1
		else:
			result.append(right[j])
			j = j + 1
	while i < len(left):
		result.append(left[i])
		i = i + 1
	while j < len(right):
		result.append(right[j])
		j = j + 1
	return result


# O(n*log(n))
def quicksort(arreglo):
	largo = len(arreglo)
	if largo == 0:
		return arreglo
	if largo == 1:
		return arreglo
	medio = largo // 2
	(menores,mayores) = filtra(arreglo[0:medio] + arreglo[medio+1:largo],arreglo[medio])
	ordenadoIzq = quicksort(menores)
	ordenadoDer = quicksort(mayores)
	return ordenadoIzq + [arreglo[medio]] + ordenadoDer


def filtra(arreglo,valor):
	menores = []
	mayores = []
	for a in arreglo:
		if a < valor:
			menores.append(a)
		else:
			mayores.append(a)
	return (menores,mayores)


