import os
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2      # bruteforce protection
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

script_dir = os.path.dirname(os.path.abspath(__file__)) 
key_file_path = os.path.join(script_dir, "key.bin")
encrypted_file_path = os.path.join(script_dir, "encrypted.bin")

with open(key_file_path, "rb") as f:
    key = f.read()

with open(encrypted_file_path, "rb") as f:
    iv = f.read(16)
    decrypt_data = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv=iv)
original = unpad(cipher.decrypt(decrypt_data), AES.block_size)
print(original)
