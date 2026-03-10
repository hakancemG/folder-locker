# Folder Locker: Python tabanli Guvenli Dosya Sifreleme Sistemi

Bu proje, yerel dizinlerdeki dosyalarin guvenligini saglamak amaciyla gelistirilmis, AES-256 (Fernet) standardini kullanan bir sifreleme cozumudur. Modern bir grafik arayuzu (GUI) ile teknik bilgisi olmayan kullanicilarin dahi verilerini kolayca koruma altina almasini saglar.

## Proje Hakkinda

Folder Locker, hassas verilerin (fotograflar, belgeler, notlar vb.) yetkisiz erisime karsi bayt seviyesinde karistirilmasi mantigiyla calisir. Uygulama, acik kaynakli ve guvenilirligi kanitlanmis kriptografik standartlari temel alir.

### Teknik Ozellikler

* Sifreleme Standarti: AES-256 tabanli Fernet (Symmetric Encryption).
* Anahtar Turetimi: PBKDF2HMAC algoritmasi ile kullanici sifresinden guvenli anahtar uretimi.
* Arayuz: CustomTkinter kutuphanesi ile modern, karanlik mod uyumlu masaustu deneyimi.
* Dosya Koruma: Sifreleme sirasinda .py, .git ve .gitignore gibi kritik sistem dosyalarinin otomatik olarak haric tutulmasi.
* Hata Yonetimi: Yanlis sifre girildiginde verinin bozulmasini onleyen dogrulama mekanizmasi.

## Kurulum ve Gereksinimler

Projenin calismasi icin sisteminizde Python 3.10 veya uzeri bir surumun yuklu olmasi onerilir.

### Bagimliliklarin Yuklenmesi

Terminal veya komut istemcisi uzerinden gerekli kutuphaneleri asagidaki komutla yukleyebilirsiniz:

pip install cryptography customtkinter

### Uygulamanin Baslatilmasi

Gerekli kutuphaneler yuklendikten sonra ana dizin icerisinde su komutu calistirin:

python gui.py

## Kullanim Kilavuzu

1. Uygulama acildiginda "Klasor Sec" butonu ile sifrelemek istediginiz dizini belirleyin.
2. Belirlediginiz guclu bir sifreyi ilgili alana girin.
3. Sifreleme islemi icin "SIFRELE" butonuna basin. Bu asamadan sonra dosyalariniz bayt seviyesinde degistirilecek ve orijinal formatlarinda acilamaz hale gelecektir.
4. Dosyalari tekrar erisilebilir hale getirmek icin ayni klasoru secip, ayni sifreyi girerek "COZ" butonuna tiklayin.

## Guvenlik Bildirimi ve Uyari

* Salt Degeri: Proje icerisinde kullanilan salt (tuz) degeri `encryptor.py` dosyasinda sabitlenmistir. Bu degerin degistirilmesi, mevcut sifreli dosyalarin bir daha asla acilamamasina neden olur.
* Sifre Hatirlatma: Sifrenizi unutmaniz durumunda verilerinizi geri dondurmenin bir yolu bulunmamaktadir.
* Git Korunumu: `.gitignore` dosyasi sayesinde gizli anahtar dosyalarinin GitHub gibi platformlara yuklenmesi engellenmistir.

## Lisans

Bu proje egitim ve kisisel kullanim amaciyla gelistirilmistir. Yazilim oldugu gibi sunulmakta olup, veri kaybi veya unutulan sifrelerden kaynakli sorumluluk kullaniciya aittir.