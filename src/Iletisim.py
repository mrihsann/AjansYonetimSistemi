
class Iletisim():
    def __init__(self,ad,soyad,tel_no,konu_basligi,konu_icerigi):
        self.ad=ad
        self.soyad=soyad
        self.__tel_no=tel_no #primary key
        self.konu_basligi=konu_basligi
        self.konu_icerigi=konu_icerigi
    def getTel_No(self): #encapsulation
        return self.__tel_no
    
    def setTel_No(self,yeni_num):
        return self.__tel_no == yeni_num
    def Mesaj_ekle(self,Dosya_adi):
       with open('Mesajlar.txt', 'a+') as f:
            f.write(f'Ad : {self.ad} ,')
            f.write(f'Soyad : {self.soyad} ,')
            f.write(f'Telefon Numarasi : {self.__tel_no} ,')
            f.write(f'Konu Basligi : {self.konu_basligi} ,')
            f.write(f'Konu Icerigi : {self.konu_icerigi} \n')
    
