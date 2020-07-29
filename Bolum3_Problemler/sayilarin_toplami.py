giris = input("Başlamak için istediğiniz sayıyı, istemiyorsanız q'ya basınız.")
toplam = 0
toplam += int(giris)
while True:
    if(giris == 'q'):
        break

    else:
        sayi = input("Toplama eklemek istediğiniz sayıyı giriniz : ")
        toplam += int(sayi)
        print("Toplam : ",toplam)
        continue