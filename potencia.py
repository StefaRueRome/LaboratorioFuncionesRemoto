
def a_power_b(a,b):
	prod=1
	
	for i in range(0,b):
		prod=prod*a
	
	return prod

while True:
	a=int(input("Ingrese la base: "))
	b=int(input("Ingrese la potencia: "))
	print(a_power_b(a,b))
	if a==0:
		break