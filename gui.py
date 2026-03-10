import customtkinter as ctk
from tkinter import filedialog, messagebox
from encryptor import FileEncryptor
import os

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Folder Locker - Güvenli Şifreleme")
        self.geometry("500x400")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Başlık
        self.label = ctk.CTkLabel(self, text="Dosya Kilitleyici", font=("Roboto", 24))
        self.label.pack(pady=20)

        # Klasör Seçimi
        self.path_entry = ctk.CTkEntry(self, placeholder_text="Klasör yolu seçilmedi...", width=350)
        self.path_entry.pack(pady=10)

        self.browse_btn = ctk.CTkButton(self, text="Klasör Seç", command=self.browse_folder)
        self.browse_btn.pack(pady=5)

        # Şifre Girişi
        self.pass_entry = ctk.CTkEntry(self, placeholder_text="Şifrenizi girin", show="*", width=350)
        self.pass_entry.pack(pady=20)

        # Butonlar (Şifrele / Çöz)
        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=10)

        self.encrypt_btn = ctk.CTkButton(self.button_frame, text="ŞİFRELE", fg_color="red", hover_color="#8B0000", command=lambda: self.start_process("encrypt"))
        self.encrypt_btn.grid(row=0, column=0, padx=10)

        self.decrypt_btn = ctk.CTkButton(self.button_frame, text="ÇÖZ", fg_color="green", hover_color="#006400", command=lambda: self.start_process("decrypt"))
        self.decrypt_btn.grid(row=0, column=1, padx=10)

    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.path_entry.delete(0, 'end')
            self.path_entry.insert(0, folder)

    def start_process(self, mode):
        path = self.path_entry.get()
        password = self.pass_entry.get()

        if not path or not password:
            messagebox.showwarning("Uyarı", "Lütfen tüm alanları doldurun!")
            return

        try:
            engine = FileEncryptor(password)
            count = 0
            
            for root, dirs, files in os.walk(path):
                for file in files:
                    if file.endswith(('.py', '.git', '.gitignore')):
                        continue
                    
                    file_path = os.path.join(root, file)
                    if mode == "encrypt":
                        engine.encrypt_file(file_path)
                    else:
                        engine.decrypt_file(file_path)
                    count += 1

            status = "kilitlendi" if mode == "encrypt" else "açıldı"
            messagebox.showinfo("Başarılı", f"{count} dosya başarıyla {status}!")
            
        except Exception as e:
            messagebox.showerror("Hata", f"İşlem başarısız! Şifre yanlış olabilir.\nDetay: {e}")

if __name__ == "__main__":
    app = App()
    app.mainloop()