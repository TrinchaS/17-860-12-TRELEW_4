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

def pares(lista):
    nuevaLista = Lista()
    nuevaLista.primero = lista.primero
    valor = nuevaLista.primero
    while valor != None:
        siguiente = valor.proximo
        if siguiente != None:
            valor.proximo = siguiente.proximo
        else:
            valor.proximo = None
        valor = valor.proximo
    return nuevaLista


#Ejercicio
#DIFÍCIL: Implementar una función que reciba una lista enlazada e invierta el orden
#(de vuelta las flechas)

def invierte(lista):
    actual = lista.primero
    siguiente = None
    if actual != None:
        siguiente = actual.proximo
        actual.proximo = None
        lista.primero = actual
    while siguiente != None: #por lo menos tengo 2 elementos
        siguiente.proximo , sig = actual , siguiente.proximo
        lista.primero = siguiente
        siguiente , actual = sig , siguiente

        #sig = siguiente.proximo
        #siguiente.proximo = actual
        #lista.primero = siguiente
        #actual = siguiente
        #siguiente = sig


nodo0 = Nodo("0")
nodo1 = Nodo("1")
nodo2 = Nodo("2")
nodo3 = Nodo("3")
nodo4 = Nodo("4")
nodo5 = Nodo("5")
nodo6 = Nodo("6")
nodo7 = Nodo("7")

listaEjemplo = Lista()

listaEjemplo.insertar_al_principio(nodo0)
listaEjemplo.inserta(1,nodo1)
listaEjemplo.inserta(2,nodo2)
listaEjemplo.inserta(3,nodo3)
listaEjemplo.inserta(4,nodo4)
listaEjemplo.inserta(5,nodo5)
listaEjemplo.inserta(6,nodo6)
listaEjemplo.inserta(7,nodo7)
print(listaEjemplo)
invierte(listaEjemplo)
print(listaEjemplo)


# FALTA
