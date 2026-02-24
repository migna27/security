from cryptography.fernet import Fernet


key= b'ThZE6CwDDN_dXdoUWoICXMVGlw6X-GPzus1qhZXCJvg='
fernet= Fernet(key)

def encrypt(value):
    return fernet.encrypt(value.encode()).decode() #

def decrypt(value):
    return fernet.decrypt(value.encode()).decode()

