ilk_Vize = int(input("İlk vize notunuzu giriniz : "))
ikinci_Vize = int(input("İkinci vize notunuzu giriniz : "))
final_Notu = int(input("Final notunuzu giriniz : "))

genel_Not = (ilk_Vize * 0.3) + (ikinci_Vize * 0.3) + (final_Notu * 0.4)

if(genel_Not > 90):
    print("Not ortalamanız : {}\nHarf Notunuz : AA".format(genel_Not))

elif(genel_Not <= 90 and genel_Not > 85):
    print("Not ortalamanız : {}\nHarf Notunuz : BA ".format(genel_Not))

elif(genel_Not <= 85 and genel_Not > 80):
    print("Not ortalamanız : {}\nHarf Notunuz : BB ".format(genel_Not))

elif(genel_Not <= 80 and genel_Not > 75):
    print("Not ortalamanız : {}\nHarf Notunuz : CB ".format(genel_Not))

elif(genel_Not <= 75 and genel_Not > 70):
    print("Not ortalamanız : {}\nHarf Notunuz : CC ".format(genel_Not))

elif(genel_Not <= 70 and genel_Not > 65):
    print("Not ortalamanız : {}\nHarf Notunuz : DC ".format(genel_Not))

elif(genel_Not <= 65 and genel_Not > 60):
    print("Not ortalamanız : {}\nHarf Notunuz : DD ".format(genel_Not))

elif(genel_Not <= 60 and genel_Not > 55):
    print("Not ortalamanız : {}\nHarf Notunuz : FF ".format(genel_Not))

else:
    print("Kaldınız.")

    