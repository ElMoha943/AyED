x=1
ventas=0
mayor=0
codigo='*'
while(x!='*'):
    x=input("Ingrese el codigo del vendedor")
    if(x!='*'): ventas=int(input("Ingrese el numero de ventas"))
    if(ventas>mayor):
       mayor = ventas
       codigo = x
    ventas=0
print("El mejor vendedor fue {} con un total de {} ventas!".format(codigo,mayor))