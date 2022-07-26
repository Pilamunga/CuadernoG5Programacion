import math 
print("_______________________________")
a=int(input("Ingrese el valor de a: "))
b=int(input("Ingrese el valor de b: "))
c=int(input("Ingrese el valor de c: "))

d=(b*b)-4*a*c


if d<0:
        print("______raiz negativa______ ")
elif a==0:
    print("______Division para cero______")
 
else:

    x1=(-b+math.sqrt(d))//((2*a))
    x2=(-b-math.sqrt(d))//((2*a))
    while True:
        if x1==x2:
            print("Unica solucion")
            print("x =", x1)
            break
        
        print("___________Dos soluciones__________")
        print("x1 = ", x1)
        print("x2 = ", x2)
        break
    
   
    

