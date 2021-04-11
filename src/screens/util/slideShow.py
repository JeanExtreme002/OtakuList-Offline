from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from .fadingEffect import FadingEffect

class SlideShow(object):

    __index = 0

    def __init__(self, widget, images, delay = 5000, transition = 1000):
        self.__widget = widget
        self.__images = [QPixmap(image) for image in images]
        self.__delay = delay
        self.__transition = transition

        self.__fading_effect = FadingEffect(self.__widget)
        self.__timer = QTimer()
        self.__timer.timeout.connect(self.__time_event)

    def __change_image(self):
        self.__widget.setPixmap(self.__images[self.__index])
        self.__index = 0 if self.__index + 1 >= len(self.__images) else (self.__index + 1)
        self.__fading_effect.fade_in(self.__transition // 2)

    def __time_event(self):
        self.__fading_effect.fade_out(self.__transition // 2, self.__change_image)

    def start(self):
        if len(self.__images) == 0: return
        self.__change_image()
        self.__timer.start(self.__delay)

    def stop(self):
        self.__timer.stop()
