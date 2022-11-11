class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.proximo = None

    def obtener_dato(self):
        return self.dato

    def __str__(self):
        return self.dato

class Lista:
    def __init__(self):
        self.primero = None

    def insertar_al_principio(self, dato):
        nuevo_nodo = Nodo(dato)
        if (self.primero != None):
            nuevo_nodo.proximo = self.primero
        self.primero = nuevo_nodo

    def obtener_primero(self):
        if (self.primero == None):
            return None
        return self.primero.dato

    #inserta un elemento en la posicion o al final si posicion en mayor a la cant. de elementos
    def inserta(self,posicion, valor):
        punteroAnterior = None
        puntero = self.primero
        pos = 0
        while pos < posicion:
            if puntero != None:
                punteroAnterior = puntero
                puntero = puntero.proximo
            pos += 1
        if pos != 0:
            punteroAnterior.proximo = valor
            valor.proximo = puntero
        else:
            self.insertar_al_principio(valor)


    #elimina segun la posicion
    def eliminar(self,posicion):
        if posicion == 0:
            if (self.primero != None):
                self.primero = self.primero.proximo
        else:
            pos = 0
            punteroAnterior = None
            puntero = self.primero
            while pos < posicion and  puntero != None:
                pos += 1
                punteroAnterior = puntero
                puntero = puntero.proximo
            if pos == posicion :
                if puntero != None :
                    punteroAnterior.proximo = puntero.proximo


    #devuelve el elemento de la posicion o None en caso de que posicion sea mayor a la cantidad de elementos
    def obtener(self,posicion):
        pos = 0
        puntero = self.primero
        while puntero != None and pos < posicion:
            puntero = puntero.proximo
            pos += 1
        if puntero != None:
            return puntero.obtener_dato()
        return None

    # por definicion el valor de Nodo no se puede modificar, entonces elimino el de la posicion y creo otro nuevo
    # si la posicion es mayor a la cantidad de elementos lo coloca al final
    def asignar(self,posicion,valor):
        self.eliminar(posicion)
        self.inserta(posicion,valor)

    def __str__(self):
        cadena = ""
        itera = self.primero
        while (itera !=  None):
            cadena += str(itera.dato) + ","
            itera = itera.proximo
        return cadena


#Ejercicio: Implementar una función que reciba una lista enlazada y retorne
#una nueva lista solo con los elementos en las posiciones pares de la original

#TERMINAR
#def pares(lista):


nodo1 = Nodo("valor 1")
nodo2 = Nodo("valor 2")
nodo3 = Nodo("valor 3")
nodo4 = Nodo("valor 4")

listaEjemplo = Lista()

listaEjemplo.insertar_al_principio(nodo1)
listaEjemplo.inserta(1,nodo2)
listaEjemplo.inserta(2,nodo3)
listaEjemplo.inserta(3,nodo4)

print(listaEjemplo)
