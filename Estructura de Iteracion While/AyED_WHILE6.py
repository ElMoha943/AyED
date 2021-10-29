#Una empresa tiene 50 viajantes que trabajan en ella. A fin de mes cada uno de los
#viajantes informa su número y los importes de cada una de las ventas realizadas. No
#se sabe la cantidad de ventas que realizó cada uno de ellos por lo que un valor de
#venta igual a cero indica que no hay más ventas de ese vendedor.
#Se pide exhibir, para cada uno de los viajantes, el Nro. del viajante y el importe de la
#mayor venta realizada por el mismo.

for i in range(50):
  max = 0
  do
    val = int(input("Ingrese el valor de una venta o 0 para salir"))
    if(val > max) max = val
  while(val!=0)
  print(f"Trabajadro N°{i}: {max}")
