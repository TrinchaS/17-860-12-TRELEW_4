def FizzBuzz_2_0(n):
    if (n%3 == 0) and (n%5 == 0):
        print('FizzBuzz')
    else:
        print(n)

def Sumatoria(j):
    n = 0
    for i in range(j+1):
        n +=i
    return n

print(Sumatoria(3))

