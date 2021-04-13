for i in range(93):
    num = int(input("Ingrese un numero"))
    if i == 0:
        Mayor = num
        Pos = i
    elif num > Mayor:
        Mayor = num
        Pos = i
print("Valor Maximo: {}\nFue ingresado en la posicion: {}".format(Mayor,Pos))
