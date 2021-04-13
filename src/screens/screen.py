from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon

class Screen(object):

    def __init__(self, ui_filename, title, icon):
        self._window = loadUi(ui_filename)
        self._window.setWindowTitle(title)
        self._window.setWindowIcon(QIcon(icon))

    def show(self):
        self._window.show()

    def close(self):
        self._window.close()
