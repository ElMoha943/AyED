total = 0
anterior = 1
for i in range (2,65):
    actual=anterior*2
    total +=actual
    anterior=actual
print(f"Dberia cobrar {total+1} granos")
