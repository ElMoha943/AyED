cantventas=0
prom=0
cantimp=0
num=-1
while(num!=0):
    num=int(input("Ingrese el importe de la venta o ingrese 0 para salir\n"))
    if(num!=0):
        cantventas+=1
        prom+=num
        if(num>30): cantimp+=1
prom=prom/cantventas
print("Se realizaron {} ventas.\nEl importe promedio fue de ${}.\n{} importes superan los $30.".format(cantventas,prom,cantimp))