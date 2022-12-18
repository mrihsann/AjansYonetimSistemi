class Personel():
    def __init__(self,personel_id,ad,soyad,yas,cinsiyet,birim,maas):
        self.personel_id=personel_id #primary key
        self.ad=ad
        self.soyad=soyad
        self.yas=yas
        self.cinsiyet=cinsiyet
        self.birim=birim
        self.maas=maas
    
    def Personel_ekle(self,Dosya_adi):
       with open('Personeller.txt', 'a+') as f:
            f.write(f'Personel ID : {self.personel_id} ,')
            f.write(f'Ad : {self.ad} ,')
            f.write(f'Soyad : {self.soyad} ,')
            f.write(f'Yas : {self.yas} ,')
            f.write(f'Cinsiyet : {self.cinsiyet} ,')
            f.write(f'Birim : {self.birim} ,')
            f.write(f'Maas : {self.maas} \n')



    def Personel_ara(self,input_id):
        satir_takip=0
        with open('Personeller.txt', 'r') as f:
            a=0
            for line in f:
                if input_id == int(line[14:19]):
                    #print("Personel bulundu")
                    a=1
                    #print(line)
                    return "{},{}".format(a,satir_takip)
                satir_takip+=1
            if a==0:
                print("Personel bulunamadı")
                return "{},{}".format(a,satir_takip)

    def Personel_sil(self,input_id):
        if Personel.Personel_ara(Personel,input_id)[0]=="0":
            pass
        else:
            lines = []
            with open('Personeller.txt', 'r') as f:
                for i, line in enumerate(f):
                    if i != int(Personel.Personel_ara(Personel,input_id)[2:]):
                        lines.append(line)
            with open('Personeller.txt', 'w') as f:
                f.writelines(lines)
        print(lines)
        print("Personel Silindi")


    def Maas_zam(self,zam_orani):
        self.maas=self.maas + (self.maas*(zam_orani/100))
        print("Maaş güncellendi. Yeni maş:",self.maas)



asd = Personel(12345,"Bugra","Yildirim",21,"Erkek",5454,"Yonetici")
asd.Personel_ekle("Personeller.txt",)
asda = Personel(34545,"Bugra","Yildirim",21,"Erkek",5454,"fotografci")
asda.Personel_ekle("Personeller.txt")
asdb = Personel(89765,"Bugra","Yildirim",21,"Erkek",5454,"sekreter")
asdb.Personel_ekle("Personeller.txt")
asdc = Personel(42345,"Bugra","Yildirim",21,"Erkek",5454,"temizlikci")
asdc.Personel_ekle("Personeller.txt")

sil=Personel.Personel_sil(Personel,12345)