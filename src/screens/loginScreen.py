from PyQt5.QtGui import QPixmap
from .screen import Screen
from .util.slideShow import SlideShow

class LoginScreen(Screen):

    def __init__(self, *args, login_function, register_function, background_images = []):
        super().__init__(*args)
        self.__login_function = login_function
        self.__register_function = register_function
        self.__background_images = background_images
        self.__load_window()

    def __load_window(self):
        self.__slideShow = SlideShow(self._window.background, self.__background_images)
        self._window.loginButton.clicked.connect(self.__login)
        self._window.registerButton.clicked.connect(self.__register)
        self.__slideShow.start()
        self._window.setFocus()

    def __send_form(self, function):

        self._window.username.setReadOnly(True)
        self._window.password.setReadOnly(True)

        username = self._window.username.text()
        password = self._window.password.text()
        remember = self._window.rememberCheckBox.isChecked()

        if not function(username, password, remember):
            self._window.username.setReadOnly(False)
            self._window.password.setReadOnly(False)

    def __register(self):
        self.__send_form(self.__register_function)

    def __login(self):
        self.__send_form(self.__login_function)
