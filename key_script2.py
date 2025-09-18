import os
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2      # bruteforce protection
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# As long as I have the salt and password, I can generate the key.
salt = b'\xb2\n\xa2(\xddqgE \xd7\x8fJ\xf2\x0b\xa2\xf0\x10`"\xc5\xc8\x08\xe8P\xb0\xcf\x1as\xcf\xf0\xf9\x8c'
password = "mypassword"

key = PBKDF2(password, salt, dkLen = 32)

script_dir = os.path.dirname(os.path.abspath(__file__)) 
encrypted_file_path = os.path.join(script_dir, "encrypted.bin")

with open(encrypted_file_path, "rb") as f:
    iv = f.read(16)
    decrypt_data = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv=iv)
original = unpad(cipher.decrypt(decrypt_data), AES.block_size)
print(original)
