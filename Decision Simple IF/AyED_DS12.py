n1 = int(input("Ingresa el primer numero \n" ))  
n2 = int(input("Ingresa el segundo numero \n" ))  
n3 = int(input("Ingresa el tercer numero \n" ))  
n4 = int(input("Ingresa el cuarto numero \n" ))  
n5 = int(input("Ingresa el quinto numero \n" ))  
n6 = int(input("Ingresa el sexto numero \n" )) 

if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5 and n1 > n6:
    mayor = n1
elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5 and n2 > n6:
    mayor = n2
elif n3 > n2 and n3 > n1 and n3 > n4 and n3 > n5 and n3 > n6:
    mayor = n3
elif n4 > n2 and n4 > n3 and n4 > n1 and n4 > n5 and n4 > n6:
    mayor = n4
elif n5 > n2 and n5 > n3 and n5 > n4 and n5 > n1 and n5 > n6:
    mayor = n5
else:
    mayor = n6
    pos = 'sexto'
print('El mayor numero ingresado fue: ', mayor)