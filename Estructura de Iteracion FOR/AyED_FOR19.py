N = int(input("ingrese la cantidad de numeros"))
num1 = int(input("ingrese el primer numero"))
maxdiff = 0
for i in range(1,N):
    num2 = int(input("ingrese el siguiente numero"))
    dif = num2 - num1
    if dif > maxdiff:
        maxdiff = dif
    num1=num2
print("Maxima diferencia: ",maxdiff)
