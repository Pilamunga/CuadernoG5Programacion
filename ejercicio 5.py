def palindromo(num):
	num_string = str(num)
	num_inverso = ""
	
	largo = len(num_string)

	for i in range(largo-1,-1,-1):
		num_inverso += num_string[i]
	return int(num_inverso)


num = int(input("Ingrese un numero: "))
if num == palindromo(num):
	print (num,"Es palindromo")
else:
	print (num,"No es palindromo")
