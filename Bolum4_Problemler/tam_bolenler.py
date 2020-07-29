def tam_bolenler(sayi):
    bolenler = list()
    
    for i in range(1,sayi):
        if(sayi % i == 0):
            bolenler.append(i)    
    return bolenler

while True:
    sayi = input("Sayı : ")
    if(sayi == 'q'):
        break

    else:
        sayi = int(sayi) 
        print("Sayının tam bölenleri", tam_bolenler(sayi))
    
