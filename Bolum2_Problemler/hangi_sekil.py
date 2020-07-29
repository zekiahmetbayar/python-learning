print("1. Üçgen\n2. Dörtgen")
hangi_Sekil = int(input("Üçgen mi Dörtgen mi sorgulayacaksınız ? "))

if(hangi_Sekil == 1):
    ilk_Kenar = float(input("Üçgenin ilk kenarı : "))
    ikinci_Kenar = float(input("Üçgenin ikinci kenarı : "))
    ucuncu_Kenar = float(input("Üçgenin üçüncü kenarı : "))

    if(ilk_Kenar + ikinci_Kenar > ucuncu_Kenar and ilk_Kenar + ucuncu_Kenar > ikinci_Kenar and ikinci_Kenar + ucuncu_Kenar > ilk_Kenar):
        if(ilk_Kenar == ikinci_Kenar or ikinci_Kenar == ucuncu_Kenar or ucuncu_Kenar == ilk_Kenar ):
            print("Böyle bir üçgen çizilebilir tipi ikizkenar üçgendir.")
        
        elif(ilk_Kenar == ikinci_Kenar and ikinci_Kenar == ucuncu_Kenar):
            print("Böyle bir üçgen çizilebilir tipi eşkenar üçgendir.")

        elif(ilk_Kenar != ikinci_Kenar and ikinci_Kenar == ucuncu_Kenar and ucuncu_Kenar == ilk_Kenar ):
            print("Böyle bir üçgen çizilebilir tipi çeşitkenar üçgendir.")
        
        elif(ilk_Kenar ** 2 + ikinci_Kenar ** 2 == ucuncu_Kenar **2 or ilk_Kenar **2 + ucuncu_Kenar **2 == ikinci_Kenar or ikinci_Kenar **2 + ucuncu_Kenar **2 == ilk_Kenar):
            print("Böyle bir üçgen çizilebilir tipi dik üçgendir.")

if(hangi_Sekil == 2):
    ilk_Kenar = float(input("Dörtgenin ilk kenarı : "))
    ikinci_Kenar = float(input("Dörtgenin ikinci kenarı : "))

    