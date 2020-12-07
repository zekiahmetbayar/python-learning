import random
import time

sum_zar = 0
while True:
    zar1 = random.randint(5,6)
    zar2 = random.randint(5,6)
    zar_at = input("Zar At -> 'A'\nProgramdan Çık -> 'Q'")
    if zar_at == 'A':
        sum_zar+=1
        print("Zarlar atılıyor....")
        time.sleep(1)
        print("Zar 1 Değer : {}\nZar 2 Değer : {} ".format(zar1,zar2))
        print("Şu ana kadar atılan zar sayısı : {} ".format(sum_zar))
        if zar1 == 6 and zar2 == 6:
            break
    else:
        break