from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64

def get_key(password):
    digest = hashes.Hash(hashes.SHA256(), backend = default_backend())
    digest.update(password)
    return base64.urlsafe_b64encode(digest.finalize())

def encrypt(data, password):
    f = Fernet(get_key(password))
    return f.encrypt(bytes(data))

def decrypt(data, password):
    f = Fernet(get_key(password))
    return f.decrypt(bytes(data))
