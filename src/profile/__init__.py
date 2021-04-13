from cryptography.fernet import Fernet

class Profile(object):

    def __init__(self, username, password, data):
        self.__fernet = Fernet(Fernet.generate_key())
        self.__encrypted_password = self.__fernet.encrypt(password.encode())
        self.__username = username
        self.__data = data

    def get_password(self):
        return self.__fernet.decrypt(self.__encrypted_password).decode()

    def get_username(self):
        return self.__username
