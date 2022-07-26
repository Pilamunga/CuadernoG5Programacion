def palindromo(_n):
    n = _n
    rev = 0
    while(n > 0):
        a = n % 10
        rev = rev * 10 + a
        n = n // 10

    return(rev)

while True:
    numero = int(input('Ingrese un numero: '))

    if numero%10 == 0: 
        numero = numero//10

    if numero == palindromo(numero) :
        print(numero,'ES palindromo')
    else :
        print(numero,'NO es palindromo')
    break

