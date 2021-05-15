a, b, años = 52, 85, 0
while(a < b):
    a+=a*0.06
    b+=b*0.04
    años+=1
    print(f"A = {a:.0f} billones B = {b:.0f} billones")
print(f"A pasara a B en {años} años.")
