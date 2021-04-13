n1 = int(input("Ingresa el primer numero \n" ))  
n2 = int(input("Ingresa el segundo numero \n" ))
n3 = int(input("Ingresa el tercer numero \n" ))
if n1 <= (n2 + n3):
    if n1(n2-n3):
        if n1 == n2 and n1 == n3:
            print('Es un triangulo equilatero')
        elif n1 == n2 or n1 == n3:
            print('Es un triangulo isoseles')
        else:
            print('Es un t riangulo escalero')
    else:
        print('No es un triangulo')
else:
    print('No es un triangulo')