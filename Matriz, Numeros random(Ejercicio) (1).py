import random
matriz=[]
while True:
    filas=int(input("Ingrese el nuemro de filas: "))
    if filas<=4 or filas >=30:
        print("El digito de las filas debe ser mayor a 4, postivo y menor a 30")

    columnas=int(input("Ingrese el numero de columnas: "))
    if columnas<=4 or columnas >=30:
        print("El digito de las filas debe ser mayor a 4, positivo y menor a 30")
        break
    
    for i in range(filas):
            for j in range(columnas):
                matriz.append([0]*columnas)

    for i in range (filas):
         for j in range(columnas):
                matriz[i][j]=random.randint(0, 100)
        
    for i in range (filas):
            for j in range(columnas):
                print(matriz[i][j],end= "\t")
            print("\n")
    break
numero_mayor=0

if matriz[i][j]>numero_mayor:
                numero_mayor+=matriz[i][j]
                fila=[i]
                columna=[j]
print("El numero mayor es: ", numero_mayor)
print("Se encuentra en la fila",fila, "y columna", columna)   
           
            