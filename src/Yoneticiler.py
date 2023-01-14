import Personeller
import Oyuncular

    
class Yoneticiler(Personeller.Personel,Oyuncular.Oyuncu):
    def __init__(self,personel_id,ad,soyad,yas,cinsiyet,birim,maas):
        super().__init__(personel_id,ad,soyad,yas,cinsiyet,birim,maas)
        
    def Oyuncu_listesi(self): #abstract method 
        with open('Oyuncular.txt', 'r') as file:
            lines = file.readlines()
        print("Oyuncu Listesi:\n")
        for line in lines:
            print(line)
"""     
deneme=Yoneticiler(12345,"ass","srt",23,"erkek","baskan",23456)
deneme.Personel_ekle("Personeller.txt")
deneme.Oyuncu_listesi()
"""