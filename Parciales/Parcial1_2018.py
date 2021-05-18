cantC = 0
cantD = 0
mayoringreso = 0

def menu():
    while True:
        while True:
            option = input("MENU\n1. Total de habitantes en todo el municipio de Rosario.\n2. Cantidad total de habitantes por tipo de vivienda.\n3. Districto con mayor ingreso mensual.\n4. Salir")
            if option == '1' or option == '2' or option == '3' or option == '0':
                break
        if(option == '1'):
            print(f"Total de habitantes: {cantC+cantD}\n")
        if(option == '2'):
            print(f"Casa: {cantC}\nDpto: {cantD}\n")
        if(option == '3'):
            print(f"Districto con mayor ingreso mensual: {mayordist} ({mayoringreso})\n")
        if(option == '0'):
            break

for i in range(1,6):
    print(f"DISTRICTO {i}")
    while True:
        nv = int(input("Ingrese un numero de vivienda o ingrese 0 para salir.\n"))
        if nv == 0:
            break
        while True:
            tv = input("Ingrese C para casa o D para departamento.\n")
            if tv =='C' or tv =='D':
                break
        cant = int(input("Ingrese la cantidad de personas que viven en la vivienda.\n"))
        if(tv == "C"):
            cantC +=cant
        else:
            cantD +=cant
        ingreso = float(input("Ingrese el ingreso monetario de la vivienda.\n"))
        if ingreso > mayoringreso:
            mayoringreso = ingreso
            mayordist = i
menu()
