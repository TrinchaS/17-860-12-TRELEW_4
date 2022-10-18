def contar_tuplas(tup):
    elementosTotal = 0
    for t in tup:
        elementosTotal += len(t)
    return (len(tup),elementosTotal)

def obtener_fizzbuzz(n):
    rta = ''
    if (n%3==0):
        rta+='Fizz'
    if (n%5==0):
        rta+='Buzz'
    if (rta!=''):
        return rta
    return n

def fizzbuzz(n):
    rta = []
    for i in range(n+1):
        rta.append(obtener_fizzbuzz(i))
    return rta

#def main():
#    n = int(input("Ingrese el n°: "))
#    print(fizzbuzz(n))

def concatenar(tup,sep):
    rta = ""
    n = len(tup)
    for t in tup:
        rta += t
        n -= 1
        if(n>0):
            rta += sep
    return rta

#print(concatenar("holalalalalal","-"))#["hola","como","estas"],"-"))


#para hacerla distinta a la de la practica
def sumar_matrices(mat1,mat2):
    rta = []
    for (m1,m2) in zip(mat1,mat2):
        rta.append(suma(m1 , m2))
    return rta

def suma(mat1,mat2):
    rta = []
    for (m1,m2) in zip(mat1,mat2):
        rta.append(m1+m2)
    return rta

print(sumar_matrices([[1,2],[3,4]],[[2,2],[1,1]]))
        

