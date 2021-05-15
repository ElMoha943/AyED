total = 0
M = int(input("Ingrese el primer numero"))
N = int(input("Ingrese el segundo numero"))
for i in range(M+1,M+N+1):
    total += i
print(total)
