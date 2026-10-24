from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)
plain_text = b"Rajalakshmi Engineering College"
encrypted_text = cipher.encrypt(plain_text)
decrypted_text = cipher.decrypt(encrypted_text)

print("Original Data:", plain_text.decode())
print("Encrypted Data:", encrypted_text.decode())
print("Decrypted Data:", decrypted_text.decode())
print("Keep the generated key safe; encrypted data cannot be decrypted without it.")
