print("""
**********************************************

ATM'ye Hoşgeldiniz ! 

1 . Bakiye Sorgula

2 . Para Yatırma

3 . Para Çekme

Uyarı : Programdan çıkmak için q tuşuna basın!

**********************************************

""")

bakiye = 1000
while True:
    islem = input("İşlemi seçiniz : ")
    if(islem == 'q'):
        print("Görüşmek üzere.")
        break

    elif(islem == "1"):
        print("Bakiyeniz {} ".format(bakiye))
    
    elif(islem == "2"):
        miktar = int(input("Miktarı giriniz : "))
        bakiye += miktar
        print(miktar)

    elif(islem == "3"):
        miktar = int(input("Miktarı giriniz : "))
        if (bakiye - miktar < 0):
            print("Yetersiz bakiye.")
            continue
        bakiye -= miktar

    
