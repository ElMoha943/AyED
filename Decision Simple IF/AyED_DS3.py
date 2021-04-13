a1 = input("Ingresa el primer angulo \n" )  
a2 = input("Ingresa el segundo angulo \n" )  
a3 = input("Ingresa el tercer angulo \n" )
if a1+a2+a3 == 180:
    if a1 == 90 or a2 == 90 or a3 == 30:
        print('El triangulo es rectangulo')
    else:
        print('El triangulo no es rectangulo')
else:
    print('No es un triangulo valido')