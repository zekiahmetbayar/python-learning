print("1. Toplama\n2. Çıkarma\n3. Çarpma\n4. Bölme")
islem_Tipi = int(input("Hangi işlemi yapmak istiyorsunuz ?"))

if(islem_Tipi > 4):
    print("Geçersiz işlem !")

ilk_Sayi = float(input("İlk sayıyı giriniz : "))
ikinci_Sayi = float(input("İkinci sayıyı giriniz : "))

if(islem_Tipi == 1):
    print("Sonuç : {} ".format(ilk_Sayi+ikinci_Sayi))

elif(islem_Tipi == 2):
    print("Sonuç : {} ".format(ilk_Sayi-ikinci_Sayi))

elif(islem_Tipi == 3):
    print("Sonuç : {} ".format(ilk_Sayi*ikinci_Sayi))

elif(islem_Tipi == 4):
    print("Sonuç : {} ".format(ilk_Sayi/ikinci_Sayi))

else:
    print("Geçersiz işlem !")
