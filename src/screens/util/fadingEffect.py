from PyQt5.QtWidgets import QGraphicsOpacityEffect
from PyQt5.QtCore import QTimer

class FadingEffect(object):

    __callback = None
    __time = 10

    def __init__(self, widget, startOpacity = 1.0):
        self.__widget = widget
        self.__opacity = startOpacity

        self.__opacityEffect = QGraphicsOpacityEffect()
        self.__opacityEffect.setOpacity(self.__opacity)
        self.__widget.setGraphicsEffect(self.__opacityEffect)

        self.__timer = QTimer()
        self.__timer.timeout.connect(self.__time_event)

    def __change_opacity(self):
        self.__opacity += self.__step
        self.__opacityEffect.setOpacity(self.__opacity)

    def __has_finished(self):
        return (self.__step < 0 and self.__opacity <= 0) or (self.__step > 0 and self.__opacity >= 1)

    def __start_animation(self, duration, callback = None, out = True):
        if duration < self.__time: duration = self.__time

        self.__callback = callback
        self.__step = (-1 if out else 1) / (duration / self.__time)
        self.__timer.start(self.__time)

    def __stop_animation(self):
        self.__opacity = 0 if self.__step < 0 else 1
        self.__timer.stop()

    def __time_event(self):
        self.__change_opacity()

        if self.__has_finished():
            self.__stop_animation()
            if callable(self.__callback): self.__callback()

    def fade_in(self, duration, callback = None):
        if self.__opacity >= 1: return
        self.__start_animation(duration, callback, False)

    def fade_out(self, duration, callback = None):
        if self.__opacity <= 0: return
        self.__start_animation(duration, callback, True)
