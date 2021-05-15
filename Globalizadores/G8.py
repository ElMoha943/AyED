total = 0
anterior = 1
for i in range (2,65):
    anterior=anterior*2
    total +=anterior
print(f"Dberia cobrar {total+1} granos")
