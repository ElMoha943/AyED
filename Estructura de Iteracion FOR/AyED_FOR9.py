cont1 = 0
cont2 = 0
for i in range(200):
    n1 = int(input("Ingrese el importe\n"))
    if n1 < 100:
        cont1=cont1+1
    else:
        cont2=cont2+1
print("Importes <$100: {}\nImportes >=$100: {}".format(cont1,cont2))
