from sympy import symbols
from sympy import integrate
from time import sleep 
def ft():
    while True:
        while True: 
            num=int(input("Digita el numero 1 para comenzar: "))
            if num<1 or num>1:
                print("Error!! ")
            else:
                break
        
        print("---------------------------------------")
        nombre=str(input("Ingresa Tu nombre: "))
        print("Hola ", nombre, ", veo que tienes problemas con las integrales trigonometricas, yo te ayudo :)")
        sleep(1)
        print("--------------------------------------")
        while True:    
            print("Que tipo de integral es: ")
            sleep(1)
            print("1.Definida: ")
            sleep(1)
            print("2.Indefinida: ")
            sleep(1)
            n=int(input("Digita 1 o 2 : "))
            sleep(1)
            print("---------------------------------")
            if n<1 or n>2:
                print("Te quiero ayudar y no colaboras por favor elige la opcion 1 o 2!!!") 
                print("---------------------------------")
            else: 
                break
            
        if n==1 :
            print("Has elegido integral definida, De acuerdo:  ")
            funcion1=input("Ingrese la funcion f(x)= ")
            x=symbols('x')
            while True:
                li=input("Ingrese el limite inferior: ")
                ls=input("Ingresa el limite superior: ")
                if li>ls:
                    print("Error el limite inferior debe ser menor a limite superior: ")
                else:
                    break
            res1=integrate(funcion1, (x, li, ls))
            print(f"La respuesta es: {res1} ")
        
        elif n==2:
            print("Has elegido integral indefinida, De acuerdo:  ")
            funcion2=input("Ingrese la funcion f(x)= ")
            x=symbols('x')
            res2=integrate(funcion2, x)
            print(f"La respuesta de la integral es: {res2} + C")
            
        

        num=int(input("Deseas calcular otra integral trigonometrica? Si(5) o No(6):"))
        if num==5:
            print("Iniciamos de nuevo :)")
        else:
            break     
ft()    