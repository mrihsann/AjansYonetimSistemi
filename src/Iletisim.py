
class Iletisim():
    def __init__(self,ad,soyad,tel_no,konu_basligi,konu_icerigi):
        self.ad=ad
        self.soyad=soyad
        self.tel_no=tel_no #primary key
        self.konu_basligi=konu_basligi
        self.konu_icerigi=konu_icerigi


    def Mesaj_ekle(self,Dosya_adi):
       with open('Mesajlar.txt', 'a+') as f:
            f.write(f'Ad : {self.ad} ,')
            f.write(f'Soyad : {self.soyad} ,')
            f.write(f'Telefon Numarasi : {self.tel_no} ,')
            f.write(f'Konu Basligi : {self.konu_basligi} ,')
            f.write(f'Konu Icerigi : {self.konu_icerigi} \n')
    
    def Mesaj_ara(self,input_id):
        satir_takip=0
        with open('Mesajlar.txt', 'r') as f:
            a=0
        
            for line in f:
                if input_id == line[49:60]:
                    #print("Mesaj bulundu")
                    a=1
                    print(line)
                    return "{},{}".format(a,satir_takip)
                satir_takip+=1
            if a==0:
                print("Mesaj bulunamadi")
                return "{},{}".format(a,satir_takip)


    def Mesaj_sil(self,input_id):
        if Iletisim.Mesaj_ara(Iletisim,input_id)[0]=="0":
            pass
        else:
            lines = []
            with open('Mesajlar.txt', 'r') as f:
                for i, line in enumerate(f):
                    if i != int(Iletisim.Mesaj_ara(Iletisim,input_id)[2:]):
                        lines.append(line)
            with open('Mesajlar.txt', 'w') as f:
                f.writelines(lines)
        for line in lines:
            print(line)
        print("Mesaj Silindi")

"""
asd = Iletisim("Bugra","Yildirim","05314700685","Erkeabjkgayvbkuak","Yoakjlvahuvbahvaşnvhjagbvyuabvi")
asd.Mesaj_ekle("Mesajlar.txt",)
asd = Iletisim("Bugra","Yildirim","05362586475","Erkek","Yonetici")
asd.Mesaj_ekle("Mesajlar.txt",)
asd = Iletisim("Bugra","Yildirim","06589654258","Erkek","Yonetici")
asd.Mesaj_ekle("Mesajlar.txt",)
asd = Iletisim("Bugra","Yildirim","03659845678","Erkek","Yonetici")
asd.Mesaj_ekle("Mesajlar.txt",)

sil=Iletisim.Mesaj_sil(Iletisim,"05314700685")  
"""