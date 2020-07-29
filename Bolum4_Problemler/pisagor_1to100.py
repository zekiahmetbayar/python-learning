dikucgen = list()

def pisagor():
    for kenar1 in range(1,101):
        for kenar2 in range(1,101):
            hipotenus = (kenar1 ** 2 + kenar2 ** 2) ** 0.5
            if(hipotenus == int(hipotenus)):
                dikucgen.append((kenar1,kenar2,hipotenus))
    
    return dikucgen
            
for i in pisagor():
    print(i)