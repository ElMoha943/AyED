# Al finalizar cada día, los vendedores de un comercio rinden al dueño sus ventas para
#calcular la comisión que cobrarán. Los vendedores son 8, codificados de la ‘A’ a la ‘H’,
#y no se sabe cuántas ventas realizó cada uno.
#Los datos vienen ordenados y agrupados por vendedor. Por cada vendedor se
#ingresan cada uno de los importes de sus ventas. Para indicar el fin de cada uno de
#ellos se ingresa un valor de venta igual a 0. Se solicita mostrar para cada uno de los
#vendedores: su código y la comisión que cobrará, que es el 2,5 % de la suma de sus
#ventas.

for i in range(8):
  total = 0
  do
    val = int(input("Ingrese el valor de una venta o 0 para salir"))
    total = total + val
  while()
  print(f"Vendedor {64+i}: {total*0.025}")
