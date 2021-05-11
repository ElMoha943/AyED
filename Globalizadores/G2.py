for i in range(100,999):
    c = i//100
    d = (i//10)%10
    u = i%10
    num = (u**3)+(d**3)+(c**3)
    if num == i:
        print(i)
