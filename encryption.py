from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"

def generate_key():
    """Generates and saves a key for encryption."""
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)

def load_key():
    """Loads an existing key or generates a new one."""
    if not os.path.exists(KEY_FILE):
        generate_key()
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()

def encrypt_password(password, key):
    """Encrypts a password."""
    f = Fernet(key)
    return f.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password, key):
    """Decrypts a password."""
    f = Fernet(key)
    return f.decrypt(encrypted_password.encode()).decode()
