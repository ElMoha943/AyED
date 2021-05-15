chars = 0
while True:
    char = input("Ingrese un caracter o ingrese un .")
    if char == '.':
        break;
    chars+=1
print(f"Cantidad de caracteres: {chars}")
