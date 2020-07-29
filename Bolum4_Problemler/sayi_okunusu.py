birler_basamagi = dict()
onlar_basamagi = dict()

birler_basamagi = {1 : "bir" , 2 : "iki" , 3 : "üç" , 4  : "dört"  , 5 : "beş" ,  6 : "altı" ,  7 : "yedi" ,  8 : "sekiz" , 9 : "dokuz"}
onlar_basamagi = {10 : "on" ,  20 : "yirmi"  , 30 : "otuz"  ,  40 :  "kırk" ,  50 : "elli"  ,  60 : "altmış"  , 70 : "yetmiş"  , 80 : "seksen" , 90 : "doksan" }

def sayi_okunusu(sayi):
    sayibirler_basamagi = sayi%10
    sayionlar_basamagi =sayi // 10

    return onlar_basamagi[sayionlar_basamagi] + birler_basamagi[sayibirler_basamagi]
while True :
    sayi = int(input("Okunuşunu öğrenmek istediğiniz sayıyı giriniz : "))
    print(sayi_okunusu(sayi))




