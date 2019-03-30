primo=0
acum_primo=0
while True:
	try:
		n=int(input("Ingrese un número: "))
		def is_prime(n):
			cont=0
			for i in range(1,n+1):
				if n%1==0:
					if n%i==0:
						cont+=1
			return cont
	
		contador=is_prime(n) 

		if contador==2:
			primo+=1
			print("1")
		else:
			if contador>2:
				print("0")
	except ValueError:
		print("-1")
	if n<=0:
		break
print("La cantidad de primos fue:",primo)

for i in range(1,primo+1):
	if primo%1==0:
		if primo%i==0:
			acum_primo+=1

if acum_primo==2:
	print("La cantidad de veces que se calcularon primos también es un número primo")
else:
	print("La cantidad de veces que se calcularon primos no es un número primo")