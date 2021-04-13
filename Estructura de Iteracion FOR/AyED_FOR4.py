cant = 0
for i in range(200):
    x = int(input("Ingrese un numero"))
    if x > 0:
        cant=cant+x
print("se ingresarton {} numeros positivos".format(cant))