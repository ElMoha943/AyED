for i in range(1,56):
    prom=0
    for j in range(1,7):
        nota = int(input("Ingrese la nota {} del alumno {}".format(j,i)))
        prom +=nota/6
    print("promedio del alumno {}: {}".format(i,prom))