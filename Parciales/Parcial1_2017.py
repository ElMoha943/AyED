obras, cuentos, fabulas, poesias, mayor = 0, 0, 0, 0, 0
escuela = 0
temp = 0
for i in range(1,11):
    print(f"ESCUELA {i}\n")
    while True:
        dni=input("Ingrese un DNI o ingrese 0 para pasar a la siguiente escuela.\n")
        if(dni=='0'):
            break;
        else:
            genero=''
            while(genero!='C' and genero!='F' and genero !='P'):
                genero=input("Ingrese un genero literario. (F: Fabula - C: Cuento - P: Poesia)\n")
            if(genero=='C'):
                cuentos+=1
            elif(genero=='F'):
                fabulas+=1
            else:
                poesias+=1
            temp+=1
            obras+=1
    if(temp>mayor):
        mayor = temp
        escuela = i
    temp=0
print("MENU\n\n1. Total de obras presentadas.\n2. Escuela que presento mayor cantidad de obras literarias.\n3. Cantidad de obras de cada genero.\n4. Salir")
while True:
    opcion=input()
    if opcion=='1':
        print(f"Total de obras presentadas {obras}")
    if opcion=='2':
        print(f"La escuela que mas obras presento fue {escuela} ({mayor} obras)")
    if opcion=='3':
        print(f"Cuentos: {cuentos}\nFabulas: {fabulas}\nPoesias: {poesias}")
    if opcion=='4':
        break;
