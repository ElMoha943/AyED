Tipo = input("Ingresa el tipo \n" )  
Medida = input("Ingresa la medida \n" )
if Tipo == 'A':
    if Medida >= 163 and Medida <= 167:
        print('Pieza Correcta')
    else:
        print('Pieza Incorrecta')
elif Tipo == 'B':
    if Medida >= 178 and Medida <=182:
        print('Pieza Correcta')
    else:
        print('Pieza Incorrecta')
else:
    print('Tipo Incorrecto')