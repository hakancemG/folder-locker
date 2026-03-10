import os
from encryptor import FileEncryptor

def process_folder(folder_path, password, mode='encrypt'):
    if not os.path.exists(folder_path):
        print("Hata: Belirtilen klasör yolu bulunamadı!")
        return 0, 0

    engine = FileEncryptor(password)
    success_count = 0
    error_count = 0
    
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Sistem ve kaynak dosyaları atlanır
            if file.endswith(('.py', '.git', '.gitignore')) or file == "secret.key":
                continue
                
            file_path = os.path.join(root, file)
            
            try:
                if mode == 'encrypt':
                    engine.encrypt_file(file_path)
                elif mode == 'decrypt':
                    engine.decrypt_file(file_path)
                success_count += 1
            except Exception:
                error_count += 1

    return success_count, error_count

if __name__ == "__main__":
    print("--- Dosya Kilitleyici Sisteme Hoş Geldiniz ---")
    target_folder = input("İşlem yapılacak klasör yolu: ")
    user_pass = input("Şifrenizi girin: ")
    action = input("İşlem seçin (e: Şifrele / d: Çöz): ").lower()

    if action == 'e':
        s_count, e_count = process_folder(target_folder, user_pass, 'encrypt')
        status_text = "kilitlendi"
    elif action == 'd':
        s_count, e_count = process_folder(target_folder, user_pass, 'decrypt')
        status_text = "açıldı"
    else:
        print("Geçersiz işlem seçildi!")
        exit()

    if s_count > 0:
        print(f"\nBaşarılı: {s_count} dosya {status_text}.")
    
    if e_count > 0:
        print(f"HATA: {e_count} dosya işlenemedi! (Şifre yanlış olabilir)")
