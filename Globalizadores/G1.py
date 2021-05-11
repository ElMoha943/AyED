while True:
    total=0
    legajo=input("Ingrese un numero de legajo o ingrese -1 para salir\n")
    if(legajo==-1):
        break
    for i in range(5):
        n=int(input(f"ingrese la nota {i+1}\n"))
        if n>=5:
            total+=1
    if total>=4:
        str = "regular"
    elif total==3:
        str = "a recuperatorio"
    else:
        str = "a recursar"
    print(f"{legajo} {str}\n")
