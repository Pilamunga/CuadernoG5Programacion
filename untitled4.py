din=int(input("Ingrese la cantidad de dinero inicial: "))
tmp=int(input("Ingrese el timepo [años]: "))
interes=float(input("Ingrese el interes :"))
meses=tmp*12
i=interes/100
T=(din*i)*meses + din   
print(f"El total de la poliza es: {T}") 

    

