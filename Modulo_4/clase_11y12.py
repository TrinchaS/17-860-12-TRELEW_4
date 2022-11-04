class Bicicleta:
	def __init__(self):
		self.ruedas = 2
		self.color = "Negra"
		self.velocidad = 10
	
	def setRuedas(self,ruedas):
		self.ruedas = ruedas
	
	def setColor(self,color):
		self.color = color

	def setVelocidad(self,velocidad):
		if 0 <= velocidad <= 80 :
			self.velocidad = velocidad
	
	def getRuedas(self):
		return self.ruedas

	def getColor(self):
		return self.color

	def getVelocidad(self):
		return self.velocidad


	########### segunda parte del ejercicio ###########

	def __str__(self):
		return "Bicicleta de " + str(self.getRuedas()) + " ruedas a " + str(self.getVelocidad()) + "km/h."

	def __eq__(self,obj):
		#chequeamos si el objecto es de la clase Bicicleta
		if isinstance(obj,Bicicleta):
			if self.ruedas == obj.ruedas and self.color == obj.color and self.velocidad == obj.velocidad:
				return True
			else:
				return False

	def __mul__(self,obj):
		#chequeamos si el objecto es de la clase Bicicleta
		if isinstance(obj,Bicicleta):
			rta = Bicicleta()
			rta.setRuedas(self.getRuedas() * obj.getRuedas())
			return rta



class Utiles:
	def __init__(self,grosor,color,tinta):
		self.grosor = grosor
		self.color = color
		self.tinta = tinta

	def escribir(self):
		pass
	
	def __str__(self):
		return "grosor: " + str(self.grosor) + " color: " + self.color + " tinta: " + str(self.tinta)


class Lapicera(Utiles):
	def __init__(self,grosor,color,tinta,disminuye):
		Utiles.__init__(self,grosor,color,tinta)
		self.disminuye = disminuye
		
	def escribir(self):
		if (self.tinta - self.disminuye > 0):
			self.tinta -= self.disminuye


class Lapiz(Utiles):
	def __init__(self,grosor,color,tinta,disminuye):
		Utiles.__init__(self,grosor,color,tinta)
		self.disminuye = disminuye
		
	def escribir(self):
		if (self.tinta - self.disminuye > 0):
			self.tinta -= self.disminuye


class Marcador(Utiles):
	def __init__(self,grosor,color,tinta,disminuye):
		Utiles.__init__(self,grosor,color,tinta)
		self.disminuye = disminuye
		
	def escribir(self):
		if (self.tinta - self.disminuye > 0):
			self.tinta -= self.disminuye


class Cartuchera:
	def __init__(self,capacidad):
		self.capacidad = capacidad
		self.elementos = []

	def agregar(self,util):
		if len(self.elementos)< self.capacidad:
			self.elementos.append(util)

	def sacar(self):
		if len(self.elementos)>0:
			self.elementos.pop()

	def __str__(self):
		rta = ""
		for n in self.elementos:
			rta += str(n) + '\n'
		return "Elementos dentro :\n" + rta

