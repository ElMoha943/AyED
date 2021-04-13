total=0
for i in range(304):
    num = int(input("Ingrese el numero de legajo"))
    altura = int(input("Ingrese la altura"))
    total=total+altura
    if altura < 165:
        print(num)
prom=total/304
print("Promedio de estaturas: ",prom)