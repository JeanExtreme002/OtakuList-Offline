class Profile(object):

    def __init__(self, username, password, data):
        self.username = username
        self.__password = password
        self.__data = data
        
