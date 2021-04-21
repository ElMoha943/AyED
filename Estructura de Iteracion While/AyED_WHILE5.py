cant, cant2, importe = 0, 0, 1
while(importe!=0):
    importe=float(input("Ingrese el importe"))
    if(importe>85):
        descuento= importe * 0.05
        cant+=1
    else: descuento = 0
    if(importe!=0) :
        cant2+=1
        print(f"Importe: {importe}\nDescuento: {descuento}\nTotal: {(importe-descuento)}")
if cant > 0 : print(f"Un {(cant/cant2)*100}% de los importes tuvieron descuento.")
else: print("No se ingresaron importes!")