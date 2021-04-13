cantidad = input("ingrese la cantidad de Kw")
if cantidad <= 200:
    precio = 0.05
elif cantidad > 200 and cantidad < 1000:
    precio = 0.1
else:
    precio = 0.15
total = cantidad * precio
print("importe", total)