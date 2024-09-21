from Crypto.Cipher import AES
import base64

def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_CFB)
    ciphertext = cipher.encrypt(message)
    return base64.b64encode(ciphertext).decode('utf-8')

def decrypt_message(ciphertext, key):
    cipher = AES.new(key, AES.MODE_CFB)
    decoded_ct = base64.b64decode(ciphertext)
    return cipher.decrypt(decoded_ct).decode('utf-8')

# Example use
key = b'Sixteen byte key'  # Ensure the key length is appropriate for AES
encrypted = encrypt_message("Sensitive data", key)
print(f"Encrypted: {encrypted}")
