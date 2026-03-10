# Folder Locker

Klasörlerinizi AES-256-GCM şifreleme algoritmasıyla kilitleyen, masaüstü arayüzüne sahip bir dosya güvenlik aracı.

---

## Genel Bakış

Folder Locker, belirlediğiniz bir klasör içindeki tüm dosyaları güçlü bir şifreleme algoritmasıyla koruma altına almanızı sağlar. Şifre çözme işlemi yalnızca doğru parola ile mümkündür; yanlış parola girişlerinde veri bütünlüğü doğrulaması devreye girer ve dosyalar bozulmaktan korunur.

Proje üç temel bileşenden oluşur: şifreleme motoru (`encryptor.py`), komut satırı arayüzü (`main.py`) ve masaüstü grafik arayüzü (`gui.py`).

---

## Özellikler

- AES-256 GCM modu ile kimlik doğrulamalı şifreleme
- PBKDF2 anahtar türetme (100.000 iterasyon, SHA-256)
- Veri bütünlüğü doğrulaması (GCM tag kontrolü)
- 64 KB'lık akış tabanlı işleme ile büyük dosya desteği
- Yinelemeli klasör tarama (alt klasörler dahil)
- Segmentli ilerleme çubuğu ve gerçek zamanlı log ekranı
- İşlem süresince UI'nin donmaması için arka plan iş parçacığı

---

## Gereksinimler

- Python 3.8 veya üzeri
- `pycryptodome`
- `customtkinter`

Bağımlılıkları yüklemek için:

```
pip install pycryptodome customtkinter
```

---

## Kullanım

**Grafik arayüz ile:**

```
python gui.py
```

Açılan pencerede klasör yolunu seçin, parolanızı girin ve "Sifrele" ya da "Coz" butonuna tıklayın. İşlem tamamlandığında log ekranında sonuçları görebilirsiniz.

**Komut satırı ile:**

```
python main.py
```

Sırasıyla klasör yolu, parola ve işlem türü (`e` şifrele / `d` çöz) girmeniz istenir.

---

## Mimari

```
folder-locker/
├── encryptor.py    # AES-GCM şifreleme ve çözme motoru
├── main.py         # Komut satırı arayüzü
└── gui.py          # customtkinter tabanlı masaüstü arayüzü
```

### encryptor.py

`FileEncryptor` sınıfı, PBKDF2 ile paroladan bir 256-bit anahtar türetir. Şifreleme sırasında her dosya için rastgele bir `nonce` üretilir ve dosyanın başına yazılır. İşlem sonunda GCM `tag` değeri dosyanın sonuna eklenerek veri bütünlüğü güvence altına alınır.

### main.py

`process_folder()` fonksiyonu belirtilen klasörü yinelemeli olarak tarar. `.py`, `.git`, `.gitignore` uzantılı dosyalar ve `secret.key` işlem dışı bırakılır. Başarılı ve başarısız işlem sayıları ayrı ayrı raporlanır.

### gui.py

`FolderLockerApp` sınıfı, `customtkinter` ile dark tema üzerine inşa edilmiştir. Dosya işleme, `threading.Thread` ile arka planda yürütülür; UI güncellemeleri `self.after()` aracılığıyla ana iş parçacığına iletilir.

---

## Güvenlik Notları

- Salt değeri sabit tanımlanmıştır. Daha yüksek güvenlik için her şifreleme işleminde rastgele salt üretilmesi ve dosyayla birlikte saklanması önerilir.
- Parola bellekte `str` olarak tutulmaktadır. Kritik ortamlarda `SecureString` benzeri bir yaklaşım değerlendirilebilir.
- Şifreli dosyalar aynı konuma, orijinal adla yazılır; orijinal içerik kalıcı olarak silinir.

---

## Yazar

Hakan Cem
