
def a_power_b(a,b):
	prod=1

	for i in range(0,b):
		if i>=10000:
			raise StopIteration("la potencia es mayor al límite")

		
		prod=prod*a
	return prod



while True:
	try:
		a=int(input("Ingrese la base: "))
		if a==0:
			print("El número es cero")
			break
			
		b=int(input("Ingrese la potencia: "))
	
	except ValueError:
		print("Ingresó una letra")
	except StopIteration:
		print("Sobrepasó el límite")
	
