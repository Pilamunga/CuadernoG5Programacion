
n=t=0 
while n<=0:
  n=int(input("Ingrese el tamaño del paquete: "))      
while t<=0:
  t=int(input("Tamaño máximo de ventana: "))
      
print ("   |",end=" ")

for i in range (1,t+1): 
  print (f"\t{n*i}",end=" ")
print()
7
for i in range (1,t*10): 
  print ("-",end=" ")
print()

for i in range (1,11): 
  print (i*10,"|",end="\t ")
  for j in range (1,t+1): 
    print (round((j*n)/(i*10),1),end="\t ")
  print()