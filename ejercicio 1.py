def potencia(B,E):
    if E==0:
        return 1
    if B<0 :
        return ("ERROR!!!")
    if E<0:
        return ("ERROR!!!")
    elif B==0:
        return 0
    elif E==1:
        return B
    else:
        return B* potencia(B, E - 1)
B=int(input("Ingrese el valor de la base : "))
E=int(input("Ingrese el valor de exponente: "))


print(potencia(B, E))
