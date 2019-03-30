"""Función que determina si un número es perfecto o no"""
def perfect_number(n):
	div=0
	for i in range(1,n):
		while n%i==0:
			div+=i
			break
	if div==n:
		print("El número es perfecto")
	else:
		print("El número no es perfecto")

n=int(input("Ingrese un número: "))

perfect_number(n)