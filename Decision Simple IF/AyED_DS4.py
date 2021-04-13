n1 = input("Ingresa el primer numero \n" )  
n2 = input("Ingresa el segundo numero \n" )  
n3 = input("Ingresa el tercer numero \n" ) 
if n1 < n2:
    if n2 < n3:
        print('Estan en orden creciente')
    else:
        print('No estan en orden creciente')
else:
    print('No estan en orden creciente')