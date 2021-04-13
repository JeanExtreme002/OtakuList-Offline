class IllegalUsernameException(Exception):

    def __init__(self, username, min_length):
        self.__username = username
        self.__min_length = min_length

    def __str__(self):
        if not self.__username.isspace() and self.__username:
            return "The username must contain at least {} characters.".format(self.__min_length)
        return "Enter an username."

class UsernameNotFoundException(Exception):

    def __init__(self, username):
        self.__username = username

    def __str__(self):
        return "This username is not registered." if self.__username else "Enter an username."

class UsernameExistsException(Exception):

    def __init__(self, username):
        self.__username = username

    def __str__(self):
        return "The username is already in use."

class IllegalPasswordException(Exception):

    def __init__(self, min_length):
        self.__min_length = min_length

    def __str__(self):
        return "The password must contain at least {} characters.".format(self.__min_length)

class InvalidPasswordException(Exception):

    def __str__(self):
        return "This password is invalid."
