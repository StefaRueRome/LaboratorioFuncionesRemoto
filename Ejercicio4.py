
def a_power_b(a,b):
	prod=1

	for i in range(0,b):
		if i>=10000:
			raise StopIteration("la potencia es mayor al límite")

		
		prod=prod*a
	return prod

par=0
impar=0
error=0
potencia=0


while True:
	try:
		potencia+=1
		a=int(input("Ingrese la base: "))
		if a==0:
			print("El número es cero")
			break
			
		b=int(input("Ingrese la potencia: "))
		resultado=a_power_b(a,b)
		print("El resultado de la potencia es: ",resultado)
		if resultado%2==0:
			par+=1
		else:
			impar+=1
	
	except ValueError:
		error+=1
		print("Ingresó una letra")
	except StopIteration:
		error+=1
		print("Sobrepasó el límite")

print("El número de potencias que se calcularon fue: ",potencia)
print("El número de pares fueron: ",par)
print("El número de impares fue: ",impar)
print("El número de errores fue: ",error)