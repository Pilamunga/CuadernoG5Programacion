import random
matriz=[]
filas=int(input("Ingrese el nuemro de filas: "))
columnas=int(input("Ingrese el numero de columnas: "))
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
    