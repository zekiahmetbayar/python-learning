#Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.
#Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)

boy = int(input("Boyunuzu giriniz : "))
kutle = int(input("Kilonuzu giriniz : "))

print("Endeks : {} ".format((kutle)/ (boy ** 2)))
