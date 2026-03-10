Folder Locker: Güvenli ve Performanslı Klasör Şifreleme Çözümü

Folder Locker, hassas verilerin gizliliğini sağlamak amacıyla geliştirilmiş, simetrik şifreleme yöntemlerini kullanan masaüstü tabanlı bir güvenlik aracıdır. Uygulama, belirtilen bir dizin altındaki tüm dosyaları özyinelemeli olarak tarar ve her birini askeri sınıf AES-256 (GCM modu) algoritması ile şifreler. Projenin temel felsefesi, yüksek boyutlu verilerde bile sistem kaynaklarını tüketmeden hızlı işlem yapabilmektir. Bu amaçla geliştirilen "Streaming" (akış) mimarisi sayesinde, gigabaytlarca boyuttaki dosyalar belleği şişirmeden 64 kilobaytlık bloklar halinde işlenir. Kullanıcı deneyimini ön planda tutan grafik arayüz ise, şifreleme işlemleri sırasında donmaları önlemek amacıyla "Multithreading" (çoklu iş parçacığı) yapısı üzerine inşa edilmiştir.
Teknik Gereksinimler ve Ortam Kurulumu

Sistemin kararlı bir şekilde çalışması için bilgisayarınızda Python 3.8 veya daha güncel bir sürümün kurulu olması gerekmektedir. Proje, şifreleme motoru için kriptografik işlemler sağlayan PyCryptodome ve modern arayüz bileşenleri için CustomTkinter kütüphanelerine ihtiyaç duyar. Yazılımın kaynak kodunu çalıştırmadan önce, sisteminizdeki paket yöneticisi aracılığıyla gerekli bağımlılıkları tamamlamalısınız. Gerekli kütüphaneleri sisteme dahil etmek için terminal üzerinden şu komutun yürütülmesi yeterlidir:

pip install customtkinter pycryptodome
Mimari Yapı ve Çalışma Prensibi

Yazılım üç ana katmandan oluşmaktadır: FileEncryptor sınıfı, işin matematiksel ve teknik mutfağını yöneterek kullanıcı şifresinden PBKDF2 ve SHA-256 algoritmalarıyla 100.000 iterasyon sonucunda güçlü bir anahtar türetir. Bu anahtar, AES-GCM moduyla birleşerek verinin hem şifrelenmesini hem de bütünlüğünün doğrulanmasını sağlar. FolderLockerApp katmanı, grafik arayüzü yönetir ve görsel olarak bölmeli ilerleme çubuğu ile işlem günlüklerini (log) anlık olarak kullanıcıya sunar. Son olarak, iş parçacığı yönetimi sayesinde ağır şifreleme yükleri ana uygulama döngüsünden izole edilerek programın tepkiselliği korunur.
Projenin Dağıtımı ve Kullanımı

Geliştirme aşaması tamamlanan yazılımı çalıştırmak için ana dizin içerisindeki arayüz dosyasını başlatmanız gerekmektedir. Projeyi bir geliştirme ortamı dışında, bağımsız bir yürütülebilir dosya olarak kullanmak isterseniz PyInstaller aracını tercih edebilirsiniz. Aşağıdaki yapılandırma komutu, kütüphane bağımlılıklarını ve tema dosyalarını tek bir paket içerisine gömerek terminal penceresi açılmayan, profesyonel bir Windows uygulaması üretir:

pyinstaller --noconsole --onefile --collect-all customtkinter --name "folder_locker" gui.py

Bu işlem sonucunda ortaya çıkan yapı, herhangi bir kurulum gerektirmeden taşınabilir bir güvenlik aracı olarak görev yapar. Programın kullanımı sırasında girilen şifrelerin veya şifreleme sırasında kullanılan "salt" (tuz) değerinin değiştirilmesi durumunda, verilerin geri döndürülemez şekilde kilitli kalacağı unutulmamalıdır.