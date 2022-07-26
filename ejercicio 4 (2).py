import math 
def Num_primo(n):
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return False
        
    return True

print("____________________________________________")
for i in range(1, 18):
    if Num_primo(i+1):
        print(i+1,"|", end="")
print()

for i in range (44, 74):
    if Num_primo(i+1):
        print(i+1,"|", end="")
print()

for i in range(74, 108):
    if Num_primo(i+1):
        print(i+1,"|", end="")
        
for i in range (108, 150):
    if Num_primo(i+1):
        print(i+1,"|", end="")
print()
print("________________________________________________")