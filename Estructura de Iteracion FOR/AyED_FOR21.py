N = int(input("Ingrese la cantidad de socios del club\n"))
Females = 0
Males = 0
Prom=0
Total = 0
for i in range(N):
    Num = int(input("Ingrese el numero de socio"))
    Edad = int(input("Ingrese la edad"))
    while True:
        Sexo = input("Ingrese el sexo (F/M)")
        if(Sexo == 'F' or Sexo == 'M'):  break
    Importe = int(input("Ingrese el importe de la cuota"))
    if(Sexo == 'F'): Females+=1
    else: Males+=1
    Prom+=Edad
    Total+=Importe
Prom=Prom/N
print("Cantidad de Hombre: {}, cantidad de mujeres: {}, promedio de edades: {}, total recaudado: {}".format(Males,Females,Prom,Total))