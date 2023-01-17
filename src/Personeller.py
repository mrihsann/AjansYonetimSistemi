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
                    return [a,satir_takip,line]
                satir_takip+=1
            if a==0:
                #print("Personel bulunamadi")
                return [a,satir_takip]

    def Personel_sil(self,input_id):
        if Personel.Personel_ara(Personel,input_id)[0]==0:
            return "Personel Bulunamadı"
        else:
            lines = []
            with open('Personeller.txt', 'r') as f:
                for i, line in enumerate(f):
                    if i != int(Personel.Personel_ara(Personel,input_id)[1]):
                        lines.append(line)

            with open('Personeller.txt', 'w') as f:
                f.writelines(lines)
        return "Personel Silindi"

