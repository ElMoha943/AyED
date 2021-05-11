silaba = input("ingrese la silaba a detectar.\n")
total=0
caracter = ''
while(caracter!='.'):
    caracter= input("ingrese un caracter.\n")
    if(caracter==silaba):
        total+=1
print(f"La silaba aparece {total} veces.")
