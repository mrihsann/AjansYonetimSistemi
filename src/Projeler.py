def index_bul(z):
            x=0
            for i in z:
                if i==",":
                    
                    break
                else:
                    x+=1
            return x

class Proje():
    def __init__(self,ad,yayin_tarihi,kategori,oyuncu_sayisi,butce,suresi):
        self.ad=ad
        self.yayin_tarihi=yayin_tarihi
        self.kategori=kategori
        self.oyuncu_sayisi=oyuncu_sayisi
        self.butce=butce
        self.suresi=suresi

    

    def Proje_Ekle(self):
        with open('Projeler.txt', 'a+') as f:
                f.write(f'Proje Ad : {self.ad} ,')
                f.write(f'Yayin Tarihi : {self.yayin_tarihi} ,')
                f.write(f'Kategori : {self.kategori} ,')
                f.write(f'Oyuncu Sayisi : {self.oyuncu_sayisi} ,')
                f.write(f'Butce : {self.butce} ,')
                f.write(f'Sure : {self.suresi} \n')

    def Proje_Ara(self,ad):
        
        satir_takip=0
        with open('Projeler.txt', 'r') as f:
            a=0
            for line in f:
                index=index_bul(line)
                if ad == line[11:index-1]:
                    a=1
                    return [a,satir_takip,line]
                satir_takip+=1
            if a==0:
                return [a,satir_takip]
    def Proje_Sil(self,ad):
        if Proje.Proje_Ara(Proje,ad)[0]==0:
            return "Proje Bulunamadı"
        else:
            lines = []
            with open('Projeler.txt', 'r') as f:
                for i, line in enumerate(f):
                    if i != int(Proje.Proje_Ara(Proje,ad)[1]):
                        lines.append(line)
            with open('Projeler.txt', 'w') as f:
                f.writelines(lines)
            return "Proje Silindi"

