x = int(input("ingrese el numero de materias"))
total=0
for i in range(x):
    nota = int(input("Ingrese la nota"))
    total=total+nota
promedio=total/x
print("Promedio: {}".format(promedio))