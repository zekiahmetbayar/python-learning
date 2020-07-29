sayi = int(input("Merak ettiğiniz sayıyı giriniz : "))
toplam = 0

for i in range(1,sayi):
    if (sayi%i == 0):
        toplam += i
    
if(toplam ==sayi):
    print(" {} sayısı mükemmel bir sayıdır. ".format(sayi))
else:
    print(" {} sayısı mükemmel bir sayı değildir. ".format(sayi))