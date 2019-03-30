def perfect_number(n):
	div=0
	for i in range(1,n):
		while n%i==0:
			div+=i
			break
	if div-n<=3:
		print("El número es casi perfecto")
	else:
		print("El número no es casi perfecto")

n=int(input("Ingrese un número: "))

perfect_number(n)