tipo = input("ingrese el tipo de cliente")
cantidad = int(input("ingrese la cantida de libros"))
bruto = int(input ("ingrese el importe bruto total"))
if tipo == 'L':
    if cantidad <= 24:
        total = bruto - (bruto * 0.2)
    else:
        total = bruto - (bruto * 0.25)
elif tipo == 'P':
    if cantidad < 6:
        total = bruto
    elif cantidad >= 6 and cantidad <= 18:
        total = bruto - (bruto * 0.05)
    else:
        total = bruto - (bruto * 0.1)
else:
    print("tipo incorrecto")