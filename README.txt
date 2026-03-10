# Folder Locker

**Hassas verilerinizi askeri sınıf şifrelemeyle koruyun.**

Folder Locker, belirtilen bir dizin altındaki tüm dosyaları özyinelemeli olarak tarayıp **AES-256 (GCM modu)** ile şifreleyen, masaüstü tabanlı bir güvenlik aracıdır. Temel tasarım felsefesi, gigabaytlarca veriyi sistem kaynaklarını tüketmeden hızlı ve güvenli biçimde işlemektir.

---

## Özellikler

- **AES-256-GCM Şifreleme** — Verinin hem şifrelenmesini hem de bütünlüğünü garanti altına alır
- **Streaming Mimarisi** — Dosyalar 64 KB'lık bloklar halinde işlenerek bellek tüketimi minimize edilir
- **PBKDF2 Anahtar Türetme** — SHA-256 ile 100.000 iterasyon; brute-force saldırılarına karşı güçlü koruma
- **Çoklu İş Parçacığı (Multithreading)** — Şifreleme yükü ana döngüden izole edilerek arayüz donmaları engellenir
- **Anlık İlerleme Takibi** — Segmentli ilerleme çubuğu ve canlı işlem günlüğü (log) ile şeffaf süreç yönetimi

---

## Gereksinimler

- Python **3.8** veya üzeri
- `pycryptodome`
- `customtkinter`

---

## Kurulum

```bash
pip install customtkinter pycryptodome
```

---

## Kullanım

### Uygulamayı Çalıştırma

```bash
python gui.py
```

### Bağımsız Yürütülebilir Dosya Oluşturma (Windows)

```bash
pyinstaller --noconsole --onefile --collect-all customtkinter --name "folder_locker" gui.py
```

Bu komut, tüm bağımlılıkları tek bir pakette toplar. Oluşan `.exe` dosyası herhangi bir Python kurulumu gerektirmez.

---

## Mimari

Uygulama üç katmandan oluşmaktadır:

| Katman | Sorumluluk |
|---|---|
| `FileEncryptor` | Anahtar türetme, AES-GCM şifreleme/çözme, dosya akışı yönetimi |
| `FolderLockerApp` | CustomTkinter arayüzü, ilerleme çubuğu, log görüntüleme |
| Thread Manager | Ağır işlemleri arka planda izole ederek UI tepkiselliğini korur |

---

## Güvenlik Notları

> **Dikkat:** Şifreleme sırasında kullanılan parola veya `salt` değeri kaybolursa veriler **geri döndürülemez biçimde kilitli kalır.** Parolanızı güvenli bir yerde saklayın.

---

## Lisans

Bu proje [MIT Lisansı](LICENSE) kapsamında dağıtılmaktadır.
