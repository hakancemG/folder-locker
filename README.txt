# Folder Locker - Python Based File Encryption System

Bu proje, yerel dizinlerde bulunan dosyaların AES-256 tabanlı Fernet algoritması kullanılarak bayt seviyesinde şifrelenmesini ve güvenli bir şekilde depolanmasını sağlayan bir masaüstü uygulamasıdır. Yazılım, hem komut satırı üzerinden hem de modern bir grafik kullanıcı arayüzü (GUI) üzerinden kontrol edilebilmektedir.

## Teknik Genel Bakış

Sistem, cryptography kütüphanesinin PBKDF2 (Password-Based Key Derivation Function 2) ve HMAC (Hash-based Message Authentication Code) protokollerini temel alır. Kullanıcı tarafından girilen düz metin şifre, SHA-256 algoritması ve sabit bir tuz (salt) değeri ile 100.000 iterasyon boyunca işlenerek 32 baytlık güvenli bir anahtara dönüştürülür.

### Temel Özellikler

1. Veri Bütünlüğü Koruması: Şifreleme sırasında verinin bozulmasını veya yanlış anahtarla açılmaya çalışıldığında kalıcı hasar görmesini engelleyen kontrol mekanizması mevcuttur.
2. Otomatik Dosya Filtreleme: Uygulama; .py (kaynak kodlar), .git (versiyon kontrol verileri) ve .gitignore gibi kritik dosyaları otomatik olarak tespit ederek şifreleme süreci dışında bırakır.
3. Modern Kullanıcı Arayüzü: CustomTkinter kütüphanesi kullanılarak geliştirilen arayüz, karanlık mod desteği ve kullanıcı dostu bir deneyim sunar.
4. Alt Dizin Desteği: Seçilen ana klasörün içindeki tüm alt klasörler recursive (özyinelemeli) olarak taranır ve hiyerarşi korunarak işlem yapılır.



## Kurulum ve Hazırlık

Uygulamanın çalışması için sisteminizde Python 3.x yüklü olmalıdır. Gerekli kütüphaneleri yüklemek için aşağıdaki komutu çalıştırın:

```bash
pip install cryptography customtkinter

Proje Yapısı

    encryptor.py: Şifreleme motoru ve anahtar üretim mantığını içeren çekirdek dosya.

    main.py: Komut satırı (CLI) üzerinden işlem yapmayı sağlayan kontrolcü.

    gui.py: Grafik kullanıcı arayüzünü başlatan ana uygulama dosyası.

    .gitignore: Hassas anahtar dosyalarının uzak sunucuya yüklenmesini engelleyen konfigürasyon.

Kullanım Talimatları
Grafik Arayüzü ile Kullanım (Önerilen)

    gui.py dosyasını çalıştırın: python gui.py

    "Klasör Seç" butonu ile şifrelemek istediğiniz dizini belirleyin.

    Güçlü bir şifre belirleyin ve ilgili alana girin.

    "ŞİFRELE" butonu ile süreci başlatın.

    Dosyaları geri döndürmek için aynı klasörü seçip aynı şifreyle "ÇÖZ" butonuna basın.

Komut Satırı ile Kullanım

    main.py dosyasını çalıştırın: python main.py

    Ekranda istenen klasör yolunu tam dizin olarak girin.

    Yapmak istediğiniz işlemi (e: şifrele / d: çöz) karakter olarak girin.

Güvenlik Uyarıları

    Salt Değeri: encryptor.py içerisinde tanımlanan salt değeri, anahtarın benzersizliğini sağlar. Bu değerin değiştirilmesi, mevcut şifreli dosyaların bir daha asla açılamamasına neden olur.

    Şifre Unutma: Uygulama, girilen şifreleri herhangi bir veritabanında saklamaz. Şifrenin unutulması durumunda veriye erişim mümkün değildir.

    Yedekleme: Kritik veriler üzerinde işlem yapmadan önce verilerin bir kopyasının yedeklenmesi tavsiye edilir.

Geliştirici Bilgileri

Bu yazılım Hakan Cem Gerçek tarafından backend geliştirme ve kriptografi pratikleri kapsamında eğitim amaçlı tasarlanmıştır.
