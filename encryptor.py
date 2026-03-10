# ==========================================
# Proje: Folder Locker - Sifreleme Motoru
# Gelistirici: Hakan Cem Gercek
# Tarih: Mart 2026
# ==========================================

import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class FileEncryptor:
    def __init__(self, password: str):
        # Şifreyi güvenli bir anahtara (key) dönüştürüyoruz
        self.key = self._generate_key(password)
        self.fernet = Fernet(self.key)

    def _generate_key(self, password: str) -> bytes:
        # Salt (tuz) değeri şifrelemeyi güçlendirir. 
        # Gerçek bir senaryoda bu sabit olmamalıdır ancak başlangıç için sabit tutuyoruz.
        salt = b'\x14\xef\xaa\x11\x92\x87\x10\x01' 
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key

    def encrypt_file(self, file_path: str):
        with open(file_path, "rb") as f:
            data = f.read()
        
        encrypted_data = self.fernet.encrypt(data)
        
        with open(file_path, "wb") as f:
            f.write(encrypted_data)

    def decrypt_file(self, file_path: str):
        with open(file_path, "rb") as f:
            data = f.read()
        
        decrypted_data = self.fernet.decrypt(data)
        
        with open(file_path, "wb") as f:
            f.write(decrypted_data)