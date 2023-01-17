from abc import ABC, abstractmethod

class Oyuncu():
    def __init__(self,tc_no,ad,soyad,yas,cinsiyet,boy,kilo,sacrenk,gozrenk,tenrenk,medenihali,tel_no,mail):
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
        self.tel_no=tel_no
        self.mail=mail
    @abstractmethod      #abstract method
    def Oyuncu_listesi(self):
        pass

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
            f.write(f'Medeni Hali : {self.medenihali},')
            f.write(f'Telefon Numarasi : {self.tel_no},')
            f.write(f'Mail Adresi : {self.mail}\n')


    def Oyuncu_ara(self,input_tc):
        satir_takip=0
        with open('Oyuncular.txt', 'r') as f:
            a=0
            for line in f:
                if input_tc == int(line[8:19]):
                    #print("oyuncu bulundu")
                    a=1
                    #print(line)
                    return [a,satir_takip,line]
                satir_takip+=1
            if a==0:
                #print("oyuncu bulunamadi")
                return [a,satir_takip]

    def Oyuncu_sil(self,input_tc):
        if Oyuncu.Oyuncu_ara(Oyuncu,input_tc)[0]=="0":
            pass
        else:
            lines = []
            with open('Oyuncular.txt', 'r') as f:
                for i, line in enumerate(f):
                    if i == int(Oyuncu.Oyuncu_ara(Oyuncu,input_tc)[1]):
                        print(line)
                    else:
                        lines.append(line)
            with open('Oyuncular.txt', 'w') as f:
                f.writelines(lines)
        print("Oyuncu Silindi")