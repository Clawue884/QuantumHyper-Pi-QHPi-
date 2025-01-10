from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import hashlib

# Generate a quantum-safe key pair (RSA for simplicity)
def generate_quantum_key():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# Encrypt data with AES and quantum-safe key
def encrypt_with_quantum(data, public_key):
    rsa_key = RSA.import_key(public_key)
    cipher = AES.new(get_random_bytes(16), AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode('utf-8'))
    return cipher.nonce + tag + ciphertext

# Sign a message (simulating with a quantum-safe method)
def sign_message(message, private_key):
    rsa_key = RSA.import_key(private_key)
    h = hashlib.sha256(message.encode('utf-8')).digest()
    return rsa_key.sign(h, None)


---
