a, e, i, o, u = 0, 0, 0, 0, 0
str = ""
while(str!='*'):
    str = input("Ingrese la siguiente letra o ingrese * para terminar")
    if str == 'A':
        a+=1
    if str == 'E':
        e+=1
    if str == 'I':
        i+=1
    if str == 'O':
        o+=1
    if str == 'U':
        u+=1
print(f"A = {a}\nE = {e}\nI = {i}\nO = {o}\nU = {u}")