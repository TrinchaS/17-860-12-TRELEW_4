def list_tupla_a_dic(tup):
    rta = {}
    for (t1,t2) in tup:
        rta[t1] = t2
    return rta

#print(list_tupla_a_dic([("a",1),("b",2),("c",3)]))

def apariciones(frase):
    fraseMin = frase.lower().replace(' ','')
    rta = {}
    for f in fraseMin:
        if f in rta:
            rta[f] += 1
        else:
            rta[f] = 1
    return rta

#print( apariciones("Hola pythonis t  as") )


def entrevista(frase1,frase2):
    fra1 = apariciones(frase1)
    fra2 = apariciones(frase2)

    for f1 in fra1:
        if not(f1 in fra2):
            return False
    return True

#print(entrevista("sol","renacimiento"))


def palabras_prohibidas(frase,prohibido):
    fra = frase.split()
    rta = []
    for f in fra:
        if f in prohibido:
            rta.append("****")
        else:
            rta.append(f)
    return " ".join(rta)

#print(palabras_prohibidas("Hoy es Lunes",{"es","azul"}))





