L1 = input("Ingresa la primer letra \n" )  
L2 = input("Ingresa la segunda letra \n" )  
L3 = input("Ingresa la tercer letra \n" ) 
if L1 > L2:
    if L2 > L3:
        print(L3,L2,L1)
    else:
        print(L2,L3,L1)
else:
    if L1 > L3:
        print(L3,L1,L2)
    elif L2 > L3:
        print(L1,L3,L2)
    else:
        print(L1,L2,L3)