ilk_Sayi = float(input("İlk sayıyı giriniz : "))
ikinci_Sayi = float(input("İkinci sayıyı giriniz : "))
ucuncu_Sayi = float(input("Üçüncü sayıyı giriniz : "))

if(ilk_Sayi > ikinci_Sayi and ilk_Sayi > ucuncu_Sayi):
    print("En büyük sayi {} dir.".format(ilk_Sayi))

if(ikinci_Sayi > ucuncu_Sayi and ikinci_Sayi > ucuncu_Sayi):
    print("En büyük sayi {} dir.".format(ikinci_Sayi))

if(ucuncu_Sayi > ilk_Sayi and ucuncu_Sayi > ikinci_Sayi):
    print("En büyük sayi {} dir.".format(ucuncu_Sayi))
