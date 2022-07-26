def Num_mayor(): 
    
    A=int(input("Ingrese el valor de A: "))
    B=int(input("Ingrese el valor de B: "))
    C=int(input("Ingrese el valor de C: "))
    
    if B<A>C:
        return A
    elif A<B>C:
        return B
    elif A<C>B:
        return C
print("_____________________________________")
print("El numero mayor es: ", Num_mayor())
print("_____________________________________")
