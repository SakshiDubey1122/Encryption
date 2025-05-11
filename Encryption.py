from cryptography.fernet import Fernet

# Original Message
message = 'Python for Security!'
print(f'Original: (message)\n')

# Generate key
key = Fernet.generate_key()
fernet = Fernet(key)

# Encrypt the message
encrypted_message = fernet.encrypt(message.encode())
print(f'Encrypted: {encrypted_message}\n')

# Decrypt the message 
decrypted_message = fernet.decrypt(encrypted_message).decode()
print(f'Decrypted: {decrypted_message}') 
