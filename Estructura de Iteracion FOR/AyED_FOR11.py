N = int(input("Ingrese la cantidad de multiplos\n"))
M = int(input("Ingrese el numero\n"))
for i in range(0,M*N,M): #Nota, si no quieren que cuente el 0 como primer multiplo cambiar a (M,M*N,M)
    print(i)