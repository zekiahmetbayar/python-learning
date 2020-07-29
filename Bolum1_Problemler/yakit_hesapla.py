# Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.

km_yakit = float(input("Kilometrede kaç tl yaktığınızı giriniz : "))
km_yol = int(input("Kaç kilometre yol yaptığınızı giriniz : "))

print("Yaktığınız toplam yakıt : {} TL'dir. ".format(km_yakit*km_yol))