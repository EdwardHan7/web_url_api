import hashlib
import base64
from Crypto.Cipher import AES
import urllib.parse

class Cryptography:

    ENCRYPTION_KEY = hashlib.sha256("A6093408C1A2AC3A69642A3902198".encode()).digest()
    SALT = bytes([99, 52, 2, 24, 51, 67, 22, 88])
    
    @staticmethod
    def encrypt_url(original_url, max_length):
        cipher = AES.new(Cryptography.ENCRYPTION_KEY, AES.MODE_ECB)
        encrypted = cipher.encrypt(Cryptography._pad(original_url.encode()))  # Convert string to bytes
        encoded = base64.b64encode(encrypted).decode("utf-8")
        encoded = urllib.parse.quote_plus(encoded)
        return encoded[:max_length]

    @staticmethod
    def _pad(s):
        block_size = 16
        remainder = len(s) % block_size
        padding_needed = block_size - remainder
        padding = bytes([padding_needed]) * padding_needed  # Using byte padding
        return s + padding
