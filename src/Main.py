import Basvuru
import Iletisim
import Menajerler
import Oyuncular
import Personeller
import Projeler
import Yoneticiler
import time

while True:
    time.sleep(2)
    print("""
----------------------------------------------------------------
1  - Oyuncu Ekle
2  - Oyuncu Ara
3  - Oyuncu Sil
4  - Oyuncu Listele
5  - Personel Ekle
6  - Personel Ara
7  - Personel Sil
8  - Proje Ekle
9 - Proje Ara
10 - Proje Sil
11 - Oyunculuk Başvurusu Yap
12 - Bizimle İletişim Kur
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
        print("Oyuncu ekleniyor...")
        time.sleep(1)
        print("Oyuncu eklendi.")
    elif girdi=="2":
        input_tc=int(input("Arama yapmak istediğiniz oyunucunun tc nosu : "))
        if Oyuncular.Oyuncu.Oyuncu_ara(Oyuncular.Oyuncu,input_tc)[0] == 1:
            print("Oyuncu bulundu")
            print(Oyuncular.Oyuncu.Oyuncu_ara(Oyuncular.Oyuncu,input_tc)[2])
        else:
            print("Oyuncu Bulunamadı")

    elif girdi=="3":
        input_tc=int(input("Silmek istediğiniz oyunucunun tc nosu : "))
        Oyuncular.Oyuncu.Oyuncu_sil(Oyuncular.Oyuncu,input_tc)

    elif girdi=="4":
        with open('Oyuncular.txt', 'r') as f:
            for line in f:
                print(line)

    elif girdi=="5":
        input_id=int(input("Personel ID giriniz:"))
        input_ad=input("Ad Giriniz : ")
        input_soyad=input("Soyad Giriniz : ")
        input_yas=int(input("Yaş giriniz : "))
        input_cinsiyet=input("Cinsiyet giriniz : ")
        input_birim=input("Birim giriniz : ")
        input_maas=int(input("Maaş giriniz : "))
        personel=Personeller.Personel(input_id,input_ad,input_soyad,input_yas,input_cinsiyet,input_birim,input_maas)
        personel.Personel_ekle("Personeller.txt")
        print("Personel ekleniyor...")
        time.sleep(1)
        print("Personel eklendi.")

    elif girdi=="6":
        input_tc=int(input("Arama yapmak istediğiniz Personelin ID no'su : "))
        if Personeller.Personel.Personel_ara(Personeller.Personel,input_tc)[0]==1:
            print("Personel Bulundu")
            print(Personeller.Personel.Personel_ara(Personeller.Personel,input_tc)[2])
        else:
            print("Personel Bulunamadı")

    elif girdi=="7":
        input_tc=int(input("Silmek istediğiniz Personelin ID no'su : "))
        print(Personeller.Personel.Personel_sil(Personeller.Personel,input_tc))

    elif girdi=="8":
        input_ad=input("Proje Adını Giriniz : ")
        input_yayin_tarihi=input("Yayın Tarihini giriniz:")
        input_kategori=input("Kategori Giriniz : ")
        input_oyuncu_sayisi=int(input("Oyuncu Sayısını giriniz : "))
        input_butce=input("Bütçe giriniz : ")
        input_sure=input("Proje süresini giriniz : ")
        proje=Projeler.Proje(input_ad,input_yayin_tarihi,input_kategori,input_oyuncu_sayisi,input_butce,input_sure)
        proje.Proje_Ekle()
        print("Proje ekleniyor...")
        time.sleep(1)
        print("Proje eklendi.")

    elif girdi=="9":
        input_ad=input("Arama yapmak istediğiniz projenin Tam Adı : ")
        if Projeler.Proje.Proje_Ara(Projeler.Proje,input_ad)[0]==1:
            print("Proje Bulundu")
            print(Projeler.Proje.Proje_Ara(Projeler.Proje,input_ad)[2])
        else:
            print("Proje Bulunamadı")

    elif girdi=="10":
        input_ad=input("Silmek istediğiniz projenin Tam Adı : ")
        print(Projeler.Proje.Proje_Sil(Projeler.Proje,input_ad))

    elif girdi=="11":
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
        basvuru = Basvuru.Basvuru(input_tc,input_ad,input_soyad,input_yas,input_cinsiyet,input_boy,input_kilo,input_sac_rengi,input_goz_rengi,input_ten_rengi,input_medeni_durumu,input_tel_no,input_mail)
        basvuru.Basvuru_ekle("Basvurular.txt")
        print("Başvuru ekleniyor...")
        time.sleep(1)
        print("Başvuru eklendi.")
    elif girdi=="12":
        input_ad=input("Adınızı Giriniz : ")
        input_soyad=input("Soyadınızı Giriniz : ")
        input_tel_no=int(input("Telefon numaranızı giriniz : "))
        input_konu_basligi=input("Konu Başlığını giriniz : ")
        input_konu_icerigi=input("Konu içeriğini giriniz : ")
        mesaj=Iletisim.Iletisim(input_ad,input_soyad,input_tel_no,input_konu_basligi,input_konu_icerigi)
        mesaj.Mesaj_ekle("Mesajlar.txt")
        print("Mesajınız iletiliyor...")
        time.sleep(1)
        print("Mesajınız iletildi.")
        

        