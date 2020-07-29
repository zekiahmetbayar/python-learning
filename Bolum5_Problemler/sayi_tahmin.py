import random # random sayı kullanmak için
import time # programa delay time eklemek için

print("""*****************

1 ile 40 arasında bir sayı tahmin et.

*****************

""")

rastgele_sayi = random.randint(1,40)
tahmin_hakki = 7
while True:
    tahmin = int(input("Tahmin : "))

    if(tahmin < rastgele_sayi):
        print("Tahmin sorgulanıyor...")
        time.sleep(1)

        print("Daha yüksek bir sayı söyleyin.")
        tahmin_hakki -=1
        print("Kalan tahmin hakkınız : ",tahmin_hakki)
    
    elif(tahmin_hakki > rastgele_sayi):
        print("Tahmin sorgulanıyor...")
        time.sleep(1)

        print("Daha alçak bir sayı söyleyin.")
        tahmin_hakki -=1
        print("Kalan tahmin hakkınız : ",tahmin_hakki)

    else:
        print("Tahmin sorgulanıyor...")
        time.sleep(1)

        print("Tebrikler ..! Doğru sayı !")
        break

    if(tahmin_hakki == 0):
        print("Tahmin hakkınız bitti, sayı {} idi.".format(rastgele_sayi))
        
