#Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.
#Hipotenüs Formülü: a^2 + b^2 = c^2

kisa_kenar = int(input("Üçgenin kısa kenarını giriniz : "))
uzun_kenar = int(input("Üçgenin uzun kenarını giriniz : "))
hipo_kenar = 0
(hipo_kenar) = (kisa_kenar ** 2) + (uzun_kenar ** 2)

print("Hipotenus : {} ".format(hipo_kenar ** 0.5))


