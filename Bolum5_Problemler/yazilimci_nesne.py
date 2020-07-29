class yazilimci():

    def __init__(self,isim,soyisim,diller,maas):
        self.isim = isim
        self.soyisim = soyisim
        self.diller = diller
        self.maas = maas

    def zam_yap(self,zam_miktari):
        self.zam_miktari = zam_miktari
        self.maas += zam_miktari

yazilimci1 = yazilimci("Zeki","Bayar",["Python","JS"],5000)
print(yazilimci1.diller)
yazilimci1.zam_yap(2000)
print(yazilimci1.maas)