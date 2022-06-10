num1=1
#Inicio del bucle while
while True:
#Una variable y un mensaje en pantalla. 
    n=int(input("Ingrese el numero de tabla: "))
#Linea con un cndicional n menores 1 
    if n<1:
#Imprimir en pantalla error si es menor a uno
        print("Error el numero debe ser positivo")
#si el numero es mayor que uno se rompe y pasa a la siguiente bucle.
    else:
        break
#Otro bucle while
while True:
#Variable m e impresion en pantalla. 
    m=int(input("Ingrese hasta que numero multiplicar: "))
#condicional para numeros menores a uno.
    if m<1:
#Imprimir en pantalla error si es menor a uno.
        print("Error el numero debe ser positivo")
#si el numero es mayor que uno se rompe y pasa a la siguiente bucle.
    else:
        break
#Bucle while para num1 menor o igual a la variable n. 
while num1<=n:
#Imprime en pantalla en # de tabla que se va a ejecutar. 
    print("La tabla de #",num1)
#varibles para los respectivos procesos algebraicos. 
    num2=1
    suma=0
    par=0
    impar=0
#Condicional while para num2 menor o igual a m.
    while num2<=m:
#Proceso algebraico. 
        r=num2*num1
#Imprimir en pantalla num1 y num2 ademas del ressultado. 
        print(num2,"x",num1,"=",r)
        num2+=1
#Condicional para sacar el promedio. 
        if r%2==0:  
            par+=1
        else:
            impar+=1
        suma+=r
    num1+=1
#Estas ultimas 4 lineas solo imprimen en pantalla el total de la suma, promedio y cuantos numeros pares e impares hay.
    print("La suma de los valores es:",suma)
    print("El promedio es:",suma//m)
    print("Hay",par,"numeros pares")
    print("Hay",impar,"numeros impares","\n")
