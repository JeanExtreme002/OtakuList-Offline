from PyQt5.QtWidgets import QApplication
from .core import appTexts, paths
from .database import Database
from .screens import LoginScreen
import json, os, random

class App(object):

    __application_data = dict()

    def __init__(self, args):
        self.__application = QApplication(args)
        self.__application_data = self.__get_application_data()
        self.__database = Database(paths.local_storage_path)

    def __get_application_data(self):
        if not os.path.exists(paths.application_data_filename):
            return self.__save_application_data()

        with open(paths.application_data_filename) as file:
            return json.load(file)

    def __save_application_data(self):
        with open(paths.application_data_filename, "w") as file:
            json.dump(self.__application_data, file)
            return self.__application_data

    def __login(self, username, password, remember = False):
        try:
            data = self.__database.login(username, password)
            # ...
        except Exception as error: pass
            # ...
        self.__application_data["remember"] = username if remember else ""
        self.__save_application_data()

    def __register(self, username, password, remember = False):
        try:
            self.__database.register(username, password)
            # ...
        except Exception as error: pass
            #...

    def __create_login_window(self):
        ui_filename = paths.login_window_ui_filename
        title = appTexts.login_window_title
        icon = paths.application_icon_filename
        background_images = paths.background_image_filenames.copy()
        background_images.sort(key = lambda value: random.random())

        self.__login_window = LoginScreen(
            ui_filename, title, icon,
            login_function = self.__login,
            register_function = self.__register,
            background_images = background_images
            )
        self.__login_window.show()

    def run(self):
        self.__create_login_window()
        return self.__application.exec_()
