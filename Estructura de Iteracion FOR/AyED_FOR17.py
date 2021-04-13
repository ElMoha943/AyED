for i in range(93):
    num = int(input("Ingrese un numero"))
    if i == 0:
        Mayor = num
        Menor = num
        Pos = i
        Pos2 = i
    elif num > Mayor:
        Mayor = num
        Pos = i
    elif num < Menor:
        Menor = num
        Pos2 = i
print("Valor Maximo: {}\nFue ingresado en la posicion: {}".format(Mayor,Pos))
print("Valor Minimo: {}\nFue ingresado en la posicion: {}".format(Menor,Pos2))
