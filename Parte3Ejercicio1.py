"""Función que determina si un número es primo o no"""
def is_prime(n):
	cont=0
	for i in range(1,n+1):
		if n%1==0:
			if n%i==0:
				cont+=1

	if cont==2:
		print("Is a prime number")
	else:
		if cont>2:
			print("Is NOT a prime number")

n=int(input("Ingrese un número: "))

is_prime(n)

