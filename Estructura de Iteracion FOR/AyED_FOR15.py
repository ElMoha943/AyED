#Nota: este ejercicio esta resuelto utilizando listas (arrays). Si tienen una version que no utilice este metodo hagan una PR para incluirla.
Fibonacci = []
for i in range(23):
    if i >= 2:
        Fibonacci.append(Fibonacci[i-1]+Fibonacci[i-2])
    else:
        Fibonacci.append(1)
    print(Fibonacci[i])