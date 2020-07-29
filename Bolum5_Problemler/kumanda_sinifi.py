import random
import time

class Kumanda():
    def __init__(self,tv_durum="Kapalı",tv_ses = 0,kanal_Listesi = ["TRT"],kanal = "TRT"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_Listesi = kanal_Listesi
        self.kanal = kanal
    
    def tv_ac(self):
        if(self.tv_durum  == "Açık"):
            print("TV zaten açık.")

        else:
            print("TV açılıyor...")
            self.tv_durum = "Açık"
    
    def tv_kapat(self):
        if(self.tv_durum  == "Kapalı"):
            print("TV zaten kapalı.")

        else:
            print("TV kapanıyor...")
            self.tv_durum = "Kapalı"
    
    def ses_ayarları(self):
        
        while True:
            cevap = input("Sesi azalt : '<' \nSesi arttır : '>'\nÇıkış : 'çıkış'\n")

            if(cevap == "<"):
                if(self.tv_ses != 0):
                    self.tv_ses -=1
                    print(self.tv_ses)

            elif(cevap == ">"):
                if(self.tv_ses != 40):
                    self.tv_ses +=1
                    print(self.tv_ses)

            else:
                print("Ses güncellendi : ",self.tv_ses)
                break
    
    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(1)

        self.kanal_Listesi.append(kanal_ismi)
        print("Kanal eklendi....")

    def rastgele_kanal(self):
        rastgele = random.randint(0,len(self.kanal_Listesi)-1)
        self.kanal = self.kanal_Listesi[rastgele]

        print("Şu an ki kanal : ", self.kanal)

    def __len__(self):
        return len(self.kanal_Listesi)

    def __str__(self):
        return "TV Durumu : {}\nTV Ses : {}\nKanal Listesi : {}\nŞu an ki kanal : {}\n ".format(self.tv_durum,self.tv_ses,self.kanal_Listesi,self.kanal)

kumanda = Kumanda()
print("""

TV Uygulaması

1 - TV Aç

2 - TV Kapat

3 - Ses Ayarları

4 - Kanal Ekle

5 - Kanal Sayısı Öğren

6 - Rastgele Kanala Geçme

7 - TV Bilgileri

* - Çıkmak için 'q' ya basın.


""")

while True:
    islem = int(input("İşlemi Seçiniz : "))
    if(islem == 'q'):
        print("Program sonlandırılıyor.")
        break

    elif(islem == 1):
        kumanda.tv_ac()
    
    elif(islem == 2):
        kumanda.tv_kapat()

    elif(islem == 3):
        kumanda.ses_ayarları()
    
    elif(islem == 4):
        kumanda.kanal_ekle()

    elif(islem == 5):
        print("Kanal Sayısı : ", len(kumanda))

    elif(islem == 6):
        kumanda.rastgele_kanal()

    elif(islem == 7):
        print(kumanda)

    else:
        print("Geçersiz İşlem ...!")