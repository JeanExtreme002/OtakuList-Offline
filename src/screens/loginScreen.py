from .screen import Screen
from .util.slideShow import SlideShow
import random

class LoginScreen(Screen):

    def __init__(self, ui_filename, title, icon, login_function, register_function, background_images = []):
        super().__init__(ui_filename, title, icon)
        self.__login_function = login_function
        self.__register_function = register_function
        self.__background_images = background_images.copy()
        self.__background_images.sort(key = lambda value: random.random())
        self.__load_window()

    def __connect_buttons(self):
        self.__login_button_connection = self._window.loginButton.clicked.connect(self.__login)
        self.__register_button_connection = self._window.registerButton.clicked.connect(self.__register)

    def __disconnect_buttons(self):
        self._window.loginButton.clicked.disconnect(self.__login_button_connection)
        self._window.registerButton.clicked.disconnect(self.__register_button_connection)

    def __lock_inputs(self, value):
        self._window.username.setReadOnly(value)
        self._window.password.setReadOnly(value)

    def __get_form_data(self):
        username = self._window.username.text()
        password = self._window.password.text()
        remember = self._window.rememberCheckBox.isChecked()
        return username, password, remember

    def __load_window(self):
        self.__connect_buttons()
        self.__slideShow = SlideShow(self._window.background, self.__background_images)
        self.__slideShow.start()
        self._window.setFocus()

    def __send_form(self, function):

        self.__disconnect_buttons()
        self.__reset_error_message()
        self.__lock_inputs(True)

        try:
            username, password, remember = self.__get_form_data()
            function(username, password, remember)
        except Exception as error:
            self.__set_error_message(error)
            self.__lock_inputs(False)
            self.__connect_buttons()

    def __register(self):
        self.__send_form(self.__register_function)

    def __login(self):
        self.__send_form(self.__login_function)

    def __reset_error_message(self):
        self._window.errorMessage.setText("")

    def __set_error_message(self, error):
        self._window.errorMessage.setText(str(error))

    def set_saved_login(self, username):
        self._window.username.setText(username)
        self._window.rememberCheckBox.setChecked(bool(username))

    def close(self):
        self.__slideShow.stop()
        self._window.close()
