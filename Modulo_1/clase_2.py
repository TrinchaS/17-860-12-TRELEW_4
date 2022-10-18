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
    for i in range(n+1):
        print(obtener_fizzbuzz(i))

#def main():
#    n = int(input("Ingrese el n°: "))
#    fizzbuzz(n)

#main()

def toSeconds(h,m,s):
    m += h * 60
    s += m * 60
    return s

def toHour(seg):
    s = seg % 60
    m = int( ((seg - s) / 60) % 60 ) 
    h = int( seg / 3600 )
    return (h,m,s)

def SumaHours(h1,m1,s1,h2,m2,s2):
    seg1 = toSeconds(h1,m1,s1)
    seg2 = toSeconds(h2,m2,s2)

    return toHour(seg1 + seg2)

def main():
    h1 = int(input("hora: "))
    m1 = int(input("minutos: "))
    s1 = int(input("segundos: "))

    h2 = int(input("hora: "))
    m2 = int(input("minutos: "))
    s2 = int(input("segundos: "))

    print(SumaHours(h1,m1,s1,h2,m2,s2))
    
main()
