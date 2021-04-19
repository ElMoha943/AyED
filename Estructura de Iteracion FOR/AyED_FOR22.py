for i in range(10):
    num = int(input("Ingrese el N° de la seccion ",i))
    cant = int(input("Ingrese la cantidad de empleados de la seccion",i))
    cantT=0
    cantM=0
    for j in range(cant):
        cantsec=0
        hours = int(input("Ingrese la cantidad de horas trabajadas del empleado ",j))
        while True:
            turno = input("Ingrese el turno del empleado (‘M’: mañana; ‘T’: tarde)")
            if(turno == 'M' or turno == 'T'): break
        if(turno == 'M'): cantM +=hours
        else: cantT+=hours
        cantsec+=hours
    cantsec/cant
    print("Horas Trabajadas en la seccion {}: {}".format(i,cantsec))
print("Horas totales del turno Mañana: {}\nHoras totales del turno Tarde: {}".format(cantM,cantT)