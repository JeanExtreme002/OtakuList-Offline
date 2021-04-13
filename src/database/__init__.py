from . import crypt, errors, util
import hashlib
import json

class Database(object):

    __data_sep = "="

    def __init__(self, path):
        self.__path = path
        self.__user_password_filename = self.__get_filename_hash("user" + util.split_dir(path)[-1]) + ".db"
        self.__user_data_filename = self.__get_filename_hash("data" + util.split_dir(path)[-1]) + ".db"
        self.__init_database()

    def __init_database(self):

        # Creates the database path if it does not exist.
        if not util.path_exists(self.__path): util.create_dir(self.__path)

    def __init_user_database(self, username):

        # Initializes the database and creates a path to save the user data.
        self.__init_database()
        util.create_dir(self.__get_user_database_path(username))

    def __get_encrypting_password(self, password) -> bytes:
        salt = "encrypting_{}_password".format(password)[::-1]
        password_hash = self.__get_password_hash(password + salt)
        return crypt.get_key(password_hash.encode())

    def __decrypt_data(self, data, password) -> str:
        encrypting_password = self.__get_encrypting_password(password)
        return crypt.decrypt(data, encrypting_password).decode()

    def __encrypt_data(self, data, password) -> bytes:
        encrypting_password = self.__get_encrypting_password(password)
        return crypt.encrypt(data.encode(), encrypting_password)

    def __remove_user_database(self, username):
        util.remove_dir(self.__get_user_database_path(username))

    def __update_user_password(self, username, password):
        with open(self.__get_user_password_filename(username), "wb") as file:
            file.write(self.__encrypt_data(self.__get_password_hash(password), username))

    def __validate_user_password(self, username, password) -> bool:
        with open(self.__get_user_password_filename(username), "rb") as file:
            return self.__decrypt_data(file.read(), username) == self.__get_password_hash(password)

    def __update_user_data(self, username, password, data):
        with open(self.__get_user_data_filename(username), "wb") as file:
            file.write(self.__encrypt_data(json.dumps(data), password + username))

    def __get_user_data(self, username, password) -> dict:
        with open(self.__get_user_data_filename(username), "rb") as file:
            return json.loads(self.__decrypt_data(file.read(), password + username))

    def __get_filename_hash(self, filename) -> str:
        salt = "file_{}_name".format(util.text_to_ascii_code(filename[::-1]))
        return hashlib.md5((filename + salt).encode()).hexdigest()

    def __get_password_hash(self, password) -> str:
        salt = "pass_{}_word".format(util.text_to_ascii_code(password[::-1]))
        return hashlib.sha512((password + salt).encode()).hexdigest()

    def __get_username_hash(self, username) -> str:
        salt = "user_{}_name".format(util.text_to_ascii_code(username[::-1]))
        return hashlib.md5((username + salt).encode()).hexdigest()

    def __get_user_database_path(self, username) -> str:
        username = self.__get_username_hash(username)
        return util.join_path(self.__path, username)

    def __get_user_password_filename(self, username) -> str:
        user_database_path = self.__get_user_database_path(username)
        return util.join_path(user_database_path, self.__user_password_filename)

    def __get_user_data_filename(self, username) -> str:
        user_database_path = self.__get_user_database_path(username)
        return util.join_path(user_database_path, self.__user_data_filename)

    def __has_user_database(self, username):
        path = self.__get_user_database_path(username)
        return util.path_exists(path)

    def __has_user_database_files(self, username):
        password_filename = self.__get_user_password_filename(username)
        data_filename = self.__get_user_data_filename(username)
        return util.path_exists(password_filename) and util.path_exists(data_filename)

    def __validate_access(self, username, password):
        new_username = username.lower()

        # Removes the user database if the database files do not exist.
        if not self.__has_user_database(new_username) or not self.__has_user_database_files(new_username):
            self.__remove_user_database(new_username)
            raise errors.UsernameNotFoundException(username)

        if not self.__validate_user_password(new_username, password):
            raise errors.InvalidPasswordException()

    def __validate_login_data(self, username = None, password = None):
        if username != None and (len(username) < 3 or username.isspace()):
            raise errors.IllegalUsernameException(username, 3)

        if password != None and (len(password) < 5 or username.isspace()):
            raise errors.IllegalPasswordException(5)

    def login(self, username, password):
        self.__validate_access(username, password)
        return self.__get_user_data(username.lower(), password)

    def register(self, username, password):
        new_username = username.lower()
        self.__validate_login_data(username, password)

        if self.__has_user_database(new_username):
            raise errors.UsernameExistsException(username)

        self.__init_user_database(new_username)
        self.__update_user_password(new_username, password)
        self.__update_user_data(new_username, password, dict())

    def remove_user(self, username, password):
        self.__validate_access(username, password)
        self.__remove_user_database(username)

    def update(self, username, password, data, new_password = None):
        self.__validate_access(username, password)

        if new_password:
            self.__validate_login_data(password = new_password)
            self.__update_user_password(username.lower(), new_password)

        self.__update_user_data(username.lower(), password if not new_password else new_password, data)
