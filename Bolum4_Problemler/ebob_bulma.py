def ebob_bul(sayi1,sayi2):

    ebob = 1
    i = 1
    while ( i <= sayi1 and  i <= sayi2):
        if( not(sayi1%i) and not(sayi2%i)):
            ebob = i
        i += 1
    return ebob

sayi1 = int(input("Sayı 1 : "))
sayi2 = int(input("Sayı 2 : "))

print("Ebob : {} ".format(ebob_bul(sayi1,sayi2)))
