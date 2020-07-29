deger1 = int(input("Ilk değer : "))
deger2 = int(input("Ikinci değer : "))
tmp = 0
print("Girdiginiz ilk değer : {}\nGirdiğiniz ikinci değer : {}".format(deger1,deger2))
print("Değerler değiştiriliyor...")

tmp = deger1
deger1 = deger2
deger2 = tmp

print("Değiştirilen ilk : {}\nDeğiştirilen ikinci değer : {}".format(deger1,deger2))