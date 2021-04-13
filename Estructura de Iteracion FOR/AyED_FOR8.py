n1 = int(input("ingrese el primer numero\n"))
n2 = int(input("ingrese el segundo numero\n"))
if n1 < n2:
    for n1 in range(n1,n2+1):
        print("{}".format(n1))