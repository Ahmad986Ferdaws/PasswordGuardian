# app/vault.py

from cryptography.fernet import Fernet
import os

# Use a static key for now, store this securely!
KEY_FILE = \"secret.key\"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, \"wb\") as f:
        f.write(key)

def load_key():
    if not os.path.exists(KEY_FILE):
        generate_key()
    with open(KEY_FILE, \"rb\") as f:
        return f.read()

def encrypt_password(plain_password: str) -> str:
    key = load_key()
    f = Fernet(key)
    encrypted = f.encrypt(plain_password.encode())
    return encrypted.decode()

def decrypt_password(encrypted_password: str) -> str:
    key = load_key()
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_password.encode())
    return decrypted.decode()

if __name__ == \"__main__\":
    generate_key()
    secret = encrypt_password(\"My$trongPassw0rd!\")
    print(\"Encrypted:\", secret)
    print(\"Decrypted:\", decrypt_password(secret))
