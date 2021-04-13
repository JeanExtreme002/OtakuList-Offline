from PyQt5.QtWidgets import QApplication
from .app.dataManager import AppDataManager
from .app.core import appTexts, paths
from .database import Database
from .profile import Profile
from .screens import LoginScreen

class App(object):

    def __init__(self, args):
        self.__application = QApplication(args)
        self.__application_data = AppDataManager(paths.application_data_filename)
        self.__database = Database(paths.local_storage_path)

    def __create_list_window(self, username, password, data):
        self.__profile = Profile(username, password, data)
        # ...
        self.__login_window.close()

    def __create_login_window(self):
        self.__login_window = LoginScreen(
            paths.login_window_ui_filename,
            appTexts.login_window_title,
            paths.application_icon_filename,
            login_function = self.__login,
            register_function = self.__register,
            background_images = paths.background_image_filenames
        )

        self.__login_window.set_saved_login(self.__application_data.get("remember"))
        self.__login_window.show()

    def __login(self, username, password, remember = False):
        data = self.__database.login(username, password)
        self.__application_data.set("remember", username if remember else "")
        self.__create_list_window(username, password, data)

    def __register(self, username, password, remember = False):
        self.__database.register(username, password)
        self.__login(username, password, remember)

    def run(self):
        self.__create_login_window()
        return self.__application.exec_()
