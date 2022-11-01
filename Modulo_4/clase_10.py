arreglo = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
nombres = ["Fede","Lucia","Alex","Simon"]
listaPrecios = [100,23,33,14,2,4,56,78]

def reemplaza(frase):
	return '@'.join(frase.split(' '))

def reversa3(vector):
	pos = 0
	rta = []
	for v in (vector):
		if (pos % 3):
			rta.append(v)
		pos += 1
	return rta[::-1]
	
def listaComprension(lista):
	return ["Hola " + l for l in lista if 'i' in l]

def paresAlCuadrado(lista):
	return map(lambda y : y**2 ,filter(lambda x : x%2 == 0,lista))

def compra(precios,saldo):
	total = 0
	for p in precios:
		total += p
	if (total > saldo):
		raise excepcion(total,saldo)
	return saldo - total

class saldoInsuficiente(Exception):
	pass

def excepcion(total,saldo):
	raise saldoInsuficiente("Saldo de " + str(saldo) + " insuficiente para la compra de " + str(total))

