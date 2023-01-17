import Personeller
class Menajerler(Personeller.Personel):
    def __init__(self,personel_id,ad,soyad,yas,cinsiyet,birim,maas,mentor_oyuncu_listesi):
        super().__init__(personel_id,ad,soyad,yas,cinsiyet,birim,maas)
        self.mentor_oyuncu_listesi=mentor_oyuncu_listesi 