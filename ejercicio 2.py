def valor():
    print("Ingresar un valor positivo: ")
valor()
num=int(input())
LFLDSMDFR=num
while LFLDSMDFR>0:
    dato=LFLDSMDFR%10
    LFLDSMDFR=(LFLDSMDFR-dato)/10
    if LFLDSMDFR%10==0:
        print("Digito: ", dato)
        
#La LFLDSMDFR es de la pelicula Lluvia de hamburguesas ajja :v