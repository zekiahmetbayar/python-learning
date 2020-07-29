print("Oyuncu Kaydetme Programı")

ad = input("Oyuncunun adı : ")
soyad = input("Oyuncunun soyadı : ")
takım  = input("Oyuncunun takımı : ")


bilgiler = [ad,soyad,takım]

print("Verdiğiniz bilgiler kaydediliyor.")

print("Oyuncu adı : {} \nOyuncu soyadı : {}\nOyuncu takımı : {}\n".format(bilgiler[0],bilgiler[1],bilgiler[2]))

print("Bilgiler Kaydedildi.")