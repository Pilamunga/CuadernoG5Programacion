def M_Burbuja(lista): 
    lista=[5,30,34,50,52,200,1001 ] 
    for i in range (len(lista)-1):
            if lista[i]> lista[i + 1]:
                   aux=lista[i]
                   lista[i]=lista[i + 1]
                   lista[i + 1]=aux
                   
    print(lista)
M_Burbuja([])
