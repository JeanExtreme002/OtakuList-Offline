import json, os

class AppDataManager(object):

    __data = dict()

    def __init__(self, filename):
        self.__filename = filename
        self.__load_data()

    def __load_data(self):
        if not os.path.exists(self.__filename): return

        with open(self.__filename) as file:
            self.__data.update(json.load(file))

    def __save_to_file(self):
        with open(self.__filename, "w") as file:
            json.dump(self.__data, file)

    def get(self, key):
        return self.__data.get(key, "")

    def set(self, key, value):
        self.__data[key] = value
        self.__save_to_file()
