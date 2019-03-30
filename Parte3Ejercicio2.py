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
			print("1")
		else:
			if contador>2:
				print("0")
	except ValueError:
		print("-1")
	if n<=0:
		break
