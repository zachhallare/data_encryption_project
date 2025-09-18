import os
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2      # bruteforce protection
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

salt = b'\xb2\n\xa2(\xddqgE \xd7\x8fJ\xf2\x0b\xa2\xf0\x10`"\xc5\xc8\x08\xe8P\xb0\xcf\x1as\xcf\xf0\xf9\x8c'
password = "mypassword"

key = PBKDF2(password, salt, dkLen=32)
message = b"Hello Secret World"

cipher = AES.new(key, AES.MODE_CBC)
ciphered_data = cipher.encrypt(pad(message, AES.block_size))

# puts the binary file in the same directory.
script_dir = os.path.dirname(os.path.abspath(__file__))
encrypted_file_path = os.path.join(script_dir, "encrypted.bin")

# encrypt.
with open(encrypted_file_path, "wb") as f:
    f.write(cipher.iv)
    f.write(ciphered_data)

# decrypt.
with open(encrypted_file_path, "rb") as f:
    iv = f.read(16)
    decrypt_data = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv=iv)
original = unpad(cipher.decrypt(decrypt_data), AES.block_size)
print(original)


key_file_path = os.path.join(script_dir, "key.bin")

with open(key_file_path, "wb") as f:
    f.write(key)
