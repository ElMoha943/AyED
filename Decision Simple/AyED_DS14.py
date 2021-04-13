n1 = input("Ingresa el primer numero \n" )  
n2 = input("Ingresa el segundo numero \n" ) 
if a > b:
    a = a - a * 0.2
else:
    b = b - b * 0.15
if a > 100 and b > 150:
    print('Valores Correctos')
else:
    print('Intervalo de riesgo')