def EsNum_primo(num):
    for n in range (2, num):
        if num%n==0:
            return False
    return True
for i in range (1, 20):
    if EsNum_primo(i + 1):
        print(i + 1, end=" ")
        
print()


