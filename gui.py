import customtkinter as ctk
from tkinter import filedialog, messagebox, Frame
from encryptor import FileEncryptor
import os
import threading

class FolderLockerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Folder Locker v2.3")
        self.geometry("540x680") # Yazı için alanı biraz daha genişlettim
        ctk.set_appearance_mode("dark")
        
        self.is_processing = False
        self._create_widgets()

    def _create_widgets(self):
        self.label = ctk.CTkLabel(self, text="Folder Locker", font=("Roboto", 28, "bold"))
        self.label.pack(pady=20)

        # Klasör Seçimi
        self.path_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.path_frame.pack(pady=5)
        self.path_entry = ctk.CTkEntry(self.path_frame, placeholder_text="Klasör yolu...", width=320)
        self.path_entry.grid(row=0, column=0, padx=10)
        self.browse_btn = ctk.CTkButton(self.path_frame, text="Seç", width=60, command=self.browse_folder)
        self.browse_btn.grid(row=0, column=1)

        # Şifre
        self.pass_entry = ctk.CTkEntry(self, placeholder_text="Şifre", show="*", width=390)
        self.pass_entry.pack(pady=10)

        # --- BÖLMELİ PROGRESS BAR ---
        self.progress_container = ctk.CTkFrame(self, fg_color="#3d3d3d", corner_radius=0, width=400, height=25)
        self.progress_container.pack(pady=15)
        
        self.segments = []
        for i in range(5):
            segment_frame = Frame(self.progress_container, bg="#3d3d3d", highlightbackground="black", highlightthickness=2, width=80, height=25)
            segment_frame.grid(row=0, column=i, sticky="nsew")
            self.segments.append(segment_frame)

        self.status_label = ctk.CTkLabel(self, text="Hazır", text_color="gray")
        self.status_label.pack(pady=(0, 5))

        # --- LOG LISTBOX ---
        self.log_box = ctk.CTkTextbox(self, width=400, height=150, font=("Consolas", 12))
        self.log_box.pack(pady=5, padx=20)
        self.log_box.configure(state="disabled")

        # Butonlar
        self.btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_frame.pack(pady=20)
        self.encrypt_btn = ctk.CTkButton(self.btn_frame, text="ŞİFRELE", fg_color="#A82828", command=lambda: self.start_process("encrypt"))
        self.encrypt_btn.grid(row=0, column=0, padx=10)
        self.decrypt_btn = ctk.CTkButton(self.btn_frame, text="ÇÖZ", fg_color="#1F9D55", command=lambda: self.start_process("decrypt"))
        self.decrypt_btn.grid(row=0, column=1, padx=10)

        # --- AUTHOR YAZISI (EN ALT) ---
        self.author_label = ctk.CTkLabel(self, text="author: Hakan Cem", font=("Roboto", 11, "italic"), text_color="#555555")
        self.author_label.pack(side="bottom", anchor="e", padx=20, pady=10)

    def add_log(self, message):
        self.log_box.configure(state="normal")
        self.log_box.insert("end", message + "\n")
        self.log_box.configure(state="disabled")
        self.log_box.see("end")

    def update_progress_bar(self, percentage):
        num_to_fill = int((percentage / 100) * len(self.segments))
        for i, segment in enumerate(self.segments):
            segment.configure(bg="#bef323" if i < num_to_fill else "#3d3d3d")

    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.path_entry.delete(0, 'end')
            self.path_entry.insert(0, folder)

    def start_process(self, mode):
        path, password = self.path_entry.get(), self.pass_entry.get()
        if not path or not password: return
        
        self._reset_ui()
        threading.Thread(target=self._worker, args=(path, password, mode), daemon=True).start()

    def _reset_ui(self):
        for segment in self.segments: segment.configure(bg="#3d3d3d")
        self.log_box.configure(state="normal")
        self.log_box.delete("1.0", "end")
        self.log_box.configure(state="disabled")
        self.encrypt_btn.configure(state="disabled")
        self.decrypt_btn.configure(state="disabled")

    def _worker(self, path, password, mode):
        try:
            engine = FileEncryptor(password)
            files_to_process = []
            for root, _, files in os.walk(path):
                for f in files:
                    if not f.endswith(('.py', '.git', '.gitignore')):
                        files_to_process.append(os.path.join(root, f))
            
            total = len(files_to_process)
            if total == 0:
                self.after(0, lambda: self.add_log("[-] Dosya bulunamadı."))
                return

            prefix = "[OK]" if mode == "encrypt" else "[UNLOCKED]"
            for i, f_path in enumerate(files_to_process):
                fname = os.path.basename(f_path)
                try:
                    if mode == "encrypt": engine.encrypt_file(f_path)
                    else: engine.decrypt_file(f_path)
                    self.after(0, lambda n=fname, p=prefix: self.add_log(f"{p} {n}"))
                except Exception:
                    self.after(0, lambda n=fname: self.add_log(f"[HATA] {n}"))
                    continue
                
                pct = ((i + 1) / total) * 100
                self.after(0, lambda p=pct: self.update_progress_bar(p))
                self.after(0, lambda n=fname: self.status_label.configure(text=f"İşleniyor: {n}"))

            self.after(0, lambda: messagebox.showinfo("Bitti", "İşlem tamamlandı."))
        except Exception as e:
            self.after(0, lambda e=e: messagebox.showerror("Hata", str(e)))
        finally:
            self.after(0, lambda: [self.encrypt_btn.configure(state="normal"), self.decrypt_btn.configure(state="normal")])

if __name__ == "__main__":
    app = FolderLockerApp()
    app.mainloop()