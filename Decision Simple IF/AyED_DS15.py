#Ingresar 3 valores en 3 variables X,Y y Z. Se desea obtener una rotación de sus
#valores, es decir que el contenido de Z pase a X, el contenido de X pase a Y, y el
#contenido de Y pase a Z. Se debe mostrar las variables X, Y y Z con sus valores
#originales y mostrar X, Y y Z con los valores luego de la rotación.

x = input("Ingrese el valor 1")
y = input("Ingrese el valor 2")
z = input("Ingrese el valor 3")

print(f"Valores Originales: x={x}, y={y}, z={z}")

aux = x
x = z
z = y
y = aux

print(f"Valores Nuevos: x={x}, y={y}, z={z}")
