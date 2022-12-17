class Oyuncu():
    def __init__(self,tc_no,ad,soyad,yas,cinsiyet,boy,kilo,sacrenk,gozrenk,tenrenk,medenihali):
        self.tc_no=tc_no #primary key
        self.ad=ad
        self.soyad=soyad
        self.yas=yas
        self.cinsiyet=cinsiyet
        self.boy=boy
        self.kilo=kilo
        self.sacrenk=sacrenk
        self.gozrenk=gozrenk
        self.tenrenk=tenrenk
        self.medenihali=medenihali
    def Oyuncu_ekle(self,Dosya_adi):
        with open('Oyuncular.txt', 'a+') as f:
            f.write(f'TC No : {self.tc_no} ,')
            f.write(f'Ad : {self.ad} ,')
            f.write(f'Soyad : {self.soyad} ,')
            f.write(f'Yas : {self.yas} ,')
            f.write(f'Cinsiyet : {self.cinsiyet} ,')
            f.write(f'Boy : {self.boy} ,')
            f.write(f'Kilo : {self.kilo} ,')
            f.write(f'Sac Renk : {self.sacrenk} ,')
            f.write(f'Goz Renk : {self.gozrenk} ,')
            f.write(f'Ten Renk : {self.tenrenk} ,')
            f.write(f'Medeni Hali : {self.medenihali}\n')

    def Oyuncu_ara(self,input_tc):
        satir_takip=0
        with open('Oyuncular.txt', 'r') as f:
            a=0
            for line in f:
                if input_tc == line[8:19]:
                    #print("oyuncu bulundu")
                    a=1
                    #print(line)
                    return "{},{}".format(a,satir_takip)
                satir_takip+=1
            if a==0:
                print("oyuncu bulunamadı")
                return "{},{}".format(a,satir_takip)

    def Oyuncu_sil(self,input_tc):
        if Oyuncu.Oyuncu_ara(Oyuncu,input_tc)[0]=="0":
            pass
        else:
            lines = []
            with open('Oyuncular.txt', 'r') as f:
                for i, line in enumerate(f):
                    if i != int(Oyuncu.Oyuncu_ara(Oyuncu,input_tc)[2:]):
                        lines.append(line)
            with open('Oyuncular.txt', 'w') as f:
                f.writelines(lines)
        print(lines)
        print("Oyuncu Silindi")


asd = Oyuncu(30514455968,"Bugra","Yildirim",21,"Erkek",187,90,"Siyah","Kahverengi","Buğday","Bekar")
asd.Oyuncu_ekle("Oyuncular.txt")
asda = Oyuncu(30514455928,"Bugra","Yildirim",21,"Erkek",187,90,"Siyah","Kahverengi","Buğday","Bekar")
asda.Oyuncu_ekle("Oyuncular.txt")
asdb = Oyuncu(36587766598,"Bugra","Yildirim",21,"Erkek",187,90,"Siyah","Kahverengi","Buğday","Bekar")
asdb.Oyuncu_ekle("Oyuncular.txt")
#arama=Oyuncu.Oyuncu_ara(Oyuncu,"30514455928")
arama=Oyuncu.Oyuncu_sil(Oyuncu,"30514455928")