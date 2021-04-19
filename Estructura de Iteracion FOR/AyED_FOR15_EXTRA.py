#Nota: este ejercicio esta resuelto utilizando listas (arrays), cosa que no dimos en clase, pero lo dejo para el que pueda interezarle.
Fibonacci = []
for i in range(23):
    if i >= 2:
        Fibonacci.append(Fibonacci[i-1]+Fibonacci[i-2])
    else:
        Fibonacci.append(1)
    print(Fibonacci[i])
