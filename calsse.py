while (1==1):
    from random import randint
    n=int(input("Ingrese el tamaño del arreglo:"))
    if n>5 or n<30:
        vector1=[ ]
        for i in range (n):
            a=randint(0, 30)
            vector1.append(a)
            print("vector1:", vector1)
        vector2=[ ]
        for j in range (n):
            b=randint(0, 30)
            vector2.append(b)            
            print("vector2:", vector2)
            
        vector3=[0]*n
        
        num=int(input("que operacion desea realizar:"))
        if num=="suma":
            for i in range(n):
                vector3[i]=vector1[i]+vector2[i]
        