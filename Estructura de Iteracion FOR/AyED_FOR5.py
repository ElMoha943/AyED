#Nota: se asume que el importe a abnoar es la suma de los 2 consumos por el precio del kw. El enunciado esta confuso y no le encuentro otro uso al medidor del mes pasado.
precio = int(input("ingrese el precio del kw"))
for i in range(1000):
    consumo1 = int(input("Ingrese el consumo del mes anterior"))
    consumo2 = int(input("Ingrese el consumo del mes actual"))
    total = consumo1+consumo2
    costo = total * precio
    print("Precio por KW: {}\nConsumo de este mes: {}\nCosto total: {}".format(precio,consumo2,costo))