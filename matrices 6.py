import random
matriz=[[int()for i in range (4)]for j in range(4)]

for filas in range(4):
    for columnas in range(4):
        matriz[filas][columnas]=random.randint(0,100)
for filas in range (4):
    for columnas in range(4):
         print(matriz[filas][columnas],"|",end=(""))
    print("\n")
     