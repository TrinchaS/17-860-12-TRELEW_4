import csv

def suma(archivo):
    rta = 0
    with open(archivo) as f:
        valor = f.readline()
        while (valor != ''):
            rta += int(valor)
            valor = f.readline()
    return rta

def funcion(lista,archivo):
    with open(archivo,"a") as ar:
        ar.write('\n')
        for l in lista:
            ar.write(l)
            ar.write('\n')
    
def filtroCSV_porPrecio(archivo,valor):
    n = int(valor)
    rta = []
    with open(archivo) as datos:
        lector = csv.DictReader(datos)
        for linea in lector:
            if int(linea["precio"]) > n:
                rta.append({"producto":linea["producto"],"precio":linea["precio"],"descripcion":linea["descripcion"]})

    with open("rta.csv","w") as fileCSV:
        titulos = ["producto","precio","descripcion"]
        escritor = csv.DictWriter(fileCSV, fieldnames=titulos)
        escritor.writeheader()
        escritor.writerows(rta)


