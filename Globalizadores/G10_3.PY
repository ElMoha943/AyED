a = e = i = o = u = pos = 0
palabra = input("Ingrese una palabra terminada en '*': ")

while palabra[pos] != "*":
    a += 1 if palabra[pos] == 'a' else 0
    e += 1 if palabra[pos] == 'e' else 0
    i += 1 if palabra[pos] == 'i' else 0
    o += 1 if palabra[pos] == 'o' else 0
    u += 1 if palabra[pos] == 'u' else 0
    pos += 1

print(f"a = {a}, e = {e}, i = {i}, o = {o}, u = {u}")