def N():
    print("n:")
    return N
N()

a=int(input())
if a<0:
    print("El valor de N debe ser positivo")
else:
    suma=0
    x=1
    for a in range (a):
        r=2**x
        x+=1
        suma=suma+r
    print("\nEl Resultado es:",suma)


