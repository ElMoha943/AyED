x, ventas, mayor, codigo = '', 0, 0, ''
while(x!='*'):
    x=input("Ingrese el codigo del vendedor")
    if(x!='*'): ventas=int(input("Ingrese el numero de ventas"))
    if(ventas>mayor):
       mayor = ventas
       codigo = x
    ventas=0
print(f"El mejor vendedor fue {codigo} con un total de {mayor} ventas!")