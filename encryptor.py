import os
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256

class FileEncryptor:
    def __init__(self, password: str):
        self.password = password
        self.salt = b'\x14\xef\xaa\x11\x92\x87\x10\x01' # Mevcut salt değerin
        self.key = PBKDF2(password, self.salt, dkLen=32, count=100000, hmac_hash_module=SHA256)

    def encrypt_file(self, file_path: str):
        cipher = AES.new(self.key, AES.MODE_GCM)
        temp_file = file_path + ".enc"
        
        with open(file_path, 'rb') as f_in, open(temp_file, 'wb') as f_out:
            # GCM modu için 'nonce' (başlangıç vektörü) dosyanın başına yazılır
            f_out.write(cipher.nonce)
            while chunk := f_in.read(64 * 1024): # 64KB'lık parçalarla oku
                f_out.write(cipher.encrypt(chunk))
            
            # Veri bütünlüğü için 'tag' eklenir
            tag = cipher.digest()
            f_out.write(tag)
            
        os.replace(temp_file, file_path)

    def decrypt_file(self, file_path: str):
        with open(file_path, 'rb') as f_in:
            nonce = f_in.read(16) # İlk 16 bayt nonce
            file_data = f_in.read()
            tag = file_data[-16:] # Son 16 bayt tag
            ciphertext = file_data[:-16]

        cipher = AES.new(self.key, AES.MODE_GCM, nonce=nonce)
        decrypted_data = cipher.decrypt_and_verify(ciphertext, tag)
        
        with open(file_path, 'wb') as f_out:
            f_out.write(decrypted_data)