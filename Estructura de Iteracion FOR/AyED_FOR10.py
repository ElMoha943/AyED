x = int(input("Ingrese el numero\n"))
cont=0
for i in range(300, 300+x+1):
    print(i)
    cont=cont+i
print("Suma: {}".format(cont))