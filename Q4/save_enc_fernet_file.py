from cryptography.fernet import Fernet

key = Fernet.generate_key()
# the key is type bytes
print("key: ", key)

with open('key.fernet', "wb") as key_file:
    key_file.write(key)