import Oyuncular
class Basvuru(Oyuncular.Oyuncu):
    def Basvuru_ekle(self,Dosya_adi):
        with open('Basvurular.txt', 'a+') as f:
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
            f.write(f'Medeni Hali : {self.medenihali},')
            f.write(f'Telefon Numarasi : {self.tel_no},')
            f.write(f'Mail Adresi : {self.mail}\n')


    def Basvuru_ara(self,input_tc):
        satir_takip=0
        with open('Basvurular.txt', 'r') as f:
            a=0
            for line in f:
                if input_tc == int(line[8:19]):
                    print("Basvuru bulundu")
                    a=1
                    #print(line)
                    return "{},{}".format(a,satir_takip)
                satir_takip+=1
            if a==0:
                print("Basvuru bulunamadi")
                return "{},{}".format(a,satir_takip)

    def Basvuru_sil(self,input_tc):
        if Basvuru.Basvuru_ara(Basvuru,input_tc)[0]=="0":
            pass
        else:
            lines = []
            with open('Basvurular.txt', 'r') as f:
                for i, line in enumerate(f):
                    if i != int(Basvuru.Basvuru_ara(Basvuru,input_tc)[2:]):
                        lines.append(line)
            with open('Basvurular.txt', 'w') as f:
                f.writelines(lines)
        for line in lines:
            print(line)
        print("Basvuru Silindi")
   
#asd = Basvuru(30514455968,"Bugra","Yildirim",21,"Erkek",187,90,"Siyah","Kahverengi","Buğday","Bekar",5462834845,"asd@gmail.com")
#asd.Basvuru_ekle("Basvurular.txt")
#asda = Basvuru(30514455928,"Bugra","Yildirim",21,"Erkek",187,90,"Siyah","Kahverengi","Buğday","Bekar",5462834845,"asd@gmail.com")
#asda.Basvuru_ekle("Basvurular.txt")
#asdb = Basvuru(36587766598,"Bugra","Yildirim",21,"Erkek",187,90,"Siyah","Kahverengi","Buğday","Bekar",5462834845,"asd@gmail.com")
#asdb.Basvuru_ekle("Basvurular.txt")
#arama=Basvuru.Basvuru_ara(Basvuru,30514455928)
#arama=Basvuru.Basvuru_sil(Basvuru,30514455928)