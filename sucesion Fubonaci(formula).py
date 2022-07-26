
from math import sqrt
def FN(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)//(2**n*sqrt(5))

def Fibonacci(numInicial, numFinal):
    n = 0
    s = FN(n)
    while s <= numFinal:
        if numInicial <= s:
            print(s)
        n += 1
        s = FN(n)
Fibonacci(1,100)

