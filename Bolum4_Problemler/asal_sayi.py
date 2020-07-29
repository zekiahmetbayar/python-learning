def asal_mi(sayi):
    if(sayi == 0 or sayi == 1):
        return False
    
    elif(sayi == 2):
        return True

    elif(sayi > 2):
        for i in range(2,sayi):
            if(sayi % i == 0):
                return False
            return True

while True :
    sayi = input("Sayı : ")

    if(sayi == 'q'):
        break
    
    else:
        sayi = int(sayi)
        if(asal_mi(sayi)):
            
            print(" {} asal bir sayıdır. ".format(sayi))
        else:
            print(" {} asal bir sayı değildir. ".format(sayi))

