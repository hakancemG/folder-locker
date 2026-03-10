# Folder Locker

AES-256 tabanlı dosya şifreleme ve çözme uygulaması. Yerel dizinlerde saklanan kişisel ve hassas verileri korumak için geliştirilmiştir.

---

## Genel Bakış

Folder Locker, seçilen bir klasördeki tüm dosyaları AES-GCM kullanarak şifreler. AES-GCM, mevcut simetrik şifreleme modları arasında en güvenli olanlardan biridir. Şifreleme anahtarı, kullanıcının girdiği paroladan PBKDF2-SHA256 algoritması ile 100.000 iterasyon uygulanarak türetilir; bu da kaba kuvvet saldırılarını hesaplama maliyeti açısından son derece zorlaştırır.

Uygulama hem grafiksel arayüz (GUI) hem de komut satırı arayüzü (CLI) ile birlikte gelir.

---

## Özellikler

- AES-256-GCM şifreleme ve kimlik doğrulamalı bütünlük doğrulama
- PBKDF2-SHA256 ile parola tabanlı anahtar türetme
- Özyinelemeli klasör işleme — alt dizinlerdeki tüm dosyalar dahil edilir
- Gerçek zamanlı ilerleme çubuğu ve dosya bazlı işlem logu
- Çok iş parçacıklı yapı — uzun işlemler sırasında GUI donmaz
- Hem GUI (`gui.py`) hem de CLI (`main.py`) giriş noktaları

---

## Proje Yapısı

```
folder-locker/
├── encryptor.py   # Çekirdek şifreleme/çözme motoru
├── main.py        # Komut satırı arayüzü
└── gui.py         # Grafiksel kullanıcı arayüzü (CustomTkinter)
```

---

## Gereksinimler

- Python 3.8 veya üstü
- pycryptodome
- customtkinter

Bağımlılıkları yüklemek için:

```
pip install pycryptodome customtkinter
```

---

## Kullanım

**Grafiksel Arayüz**

```
python gui.py
```

1. "Seç" butonuna tıklayarak hedef klasörü seçin.
2. Parolanızı girin.
3. Şifrelemek için "ŞİFRELE", çözmek için "ÇÖZ" butonuna tıklayın.

**Komut Satırı Arayüzü**

```
python main.py
```

Klasör yolu, parola ve işlem türünü (`e` şifrele / `d` çöz) girmek için yönergeleri takip edin.

---

## Güvenlik Notları

- Şifreleme ve çözme işlemlerinde aynı parola kullanılmalıdır. Parola kurtarma mekanizması bulunmamaktadır.
- Her dosya, rastgele üretilen benzersiz bir nonce ile şifrelenir. Bu sayede aynı dosya iki kez şifrelendiğinde farklı şifreli metin üretilir.
- GCM kimlik doğrulama etiketi her şifreli dosyanın sonuna eklenir; çözme sırasında dosyanın değiştirilip değiştirilmediği bu sayede tespit edilir.
- `.py`, `.git` ve `.gitignore` uzantılı dosyalar işlem dışı bırakılır; bu sayede uygulamanın kendi dosyaları yanlışlıkla bozulmaz.

---

## Geliştirici

Hakan Cem Gerçek
