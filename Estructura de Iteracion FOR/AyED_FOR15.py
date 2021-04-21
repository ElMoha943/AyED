Suma = 0
N1 = 0
N2 = 1
print(N1)
print(N2)
for i in range(3,23):
    Suma = N1 + N2
    N1 = N2
    N2 = Suma
    print(Suma)
