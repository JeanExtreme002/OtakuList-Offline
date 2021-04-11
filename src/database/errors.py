class IllegalUsernameException(Exception):

    def __init__(self, minimum):
        self.__minimum = minimum

    def __str__(self):
        return "The username must contain at least {} characters.".format(self.__minimum)

class UsernameNotFoundException(Exception):

    def __init__(self, username):
        self.__username = username

    def __str__(self):
        return "User \"{}\" does not exist.".format(self.__username)

class UsernameExistsException(Exception):

    def __init__(self, username):
        self.__username = username

    def __str__(self):
        return "The username \"{}\" is already in use.".format(self.__username)

class IllegalPasswordException(Exception):

    def __init__(self, minimum):
        self.__minimum = minimum

    def __str__(self):
        return "The password must contain at least {} characters.".format(self.__minimum)

class InvalidPasswordException(Exception):

    def __str__(self):
        return "This password is invalid."
