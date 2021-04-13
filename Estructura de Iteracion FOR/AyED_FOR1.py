remu = int(input("ingrese la remuneracion por hora\n"))
for i in range(50):
    horas = int(input("ingrese las horas trabajadas del operario\n"))
    sueldo = horas * remu
    print("sueldo del operario N°{}: {}".format(i,sueldo))