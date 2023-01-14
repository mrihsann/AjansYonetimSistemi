import Basvuru
import Iletisim
import Menajerler
import Oyuncular
import Personeller
import Projeler
import Yoneticiler



while True:
    print("""






1  - Oyuncu Ekle
2  - Oyuncu Ara
3  - Oyuncu Sil
4  - Oyuncu Listele
5  - Personel Ekle
6  - Personel Ara
7  - Personel Sil
8  - Personele Zam Yap
9  - Proje Ekle
10 - Proje Ara
11 - Proje Sil
12 - Oyunculuk Başvurusu Yap
13 - Bizimle İletişim Kur
14 - Gelen Kutusunda Mesaj Ara
15 - Gelen Kutusundan Mesaj Sil
Programdan Çıkmak İçin "DUR" yazın.
Yapmak istediğiniz işlemi seçin:
""")
    girdi=input("iŞLEM:")
    if girdi=="DUR":
        break
    elif girdi=="1":
        input_tc=int(input("TC no giriniz:"))
        input_ad=input("Adınızı Giriniz : ")
        input_soyad=input("Soyadınızı Giriniz : ")
        input_yas=int(input("Yaşınızı giriniz : "))
        input_cinsiyet=input("Cinsiyetinizi giriniz : ")
        input_boy=int(input("Boyunuzu giriniz : "))
        input_kilo=int(input("Kilonuzu giriniz : "))
        input_sac_rengi=input("Saç Renginizi giriniz : ")
        input_goz_rengi=input("Göz Renginizi giriniz : ")
        input_ten_rengi=input("Ten Renginizi giriniz : ")
        input_medeni_durumu=input("Medeni Durumunuzu giriniz.(Evli/Bekar) : ")
        input_tel_no=int(input("telefon numaranızı giriniz.(525xxxxxxx) : "))
        input_mail=input("mail adresinizi giriniz : ")
        asd = Oyuncular.Oyuncu(input_tc,input_ad,input_soyad,input_yas,input_cinsiyet,input_boy,input_kilo,input_sac_rengi,input_goz_rengi,input_ten_rengi,input_medeni_durumu,input_tel_no,input_mail)
        asd.Oyuncu_ekle("Oyuncular.txt")
    
    elif girdi=="2":
        input_tc=int(input("Arama yapmak istediğiniz oyunucunun tc no : "))
        Oyuncular.Oyuncu.Oyuncu_ara(Oyuncular.Oyuncu,input_tc)
        




"""
    elif girdi=="3":
    elif girdi=="4":
    elif girdi=="5":
    elif girdi=="6":
    elif girdi=="7":
    elif girdi=="8":
    elif girdi=="9":
    elif girdi=="10":
    elif girdi=="11":
    elif girdi=="12":
    elif girdi=="13":
    elif girdi=="14":
    elif girdi=="15":





"""