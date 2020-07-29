#Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.

#Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

#BKİ 18.5'un altındaysa -------> Zayıf

#BKİ 18.5 ile 25 arasındaysa ------> Normal

#BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

#BKİ 30'un üstündeyse -------------> Obez

boy = float(input("Boyunuzu giriniz : "))
kutle = float(input("Kilonuzu giriniz : "))
endeks = (kutle)/ (boy ** 2)

if(endeks <= 18.5):
    print("Endeks : {} , Zayıf.".format(endeks))

elif(endeks > 18.5 and endeks <= 25):
    print("Endeks : {} , Normal.".format(endeks))

elif(endeks > 25 and endeks <= 30):
    print("Endeks : {} , Fazla Kilolu.".format(endeks))

elif(endeks > 30):
    print("Endeks : {} , Obez.".format(endeks))

else: 
    print("Geçersiz işlem !")


