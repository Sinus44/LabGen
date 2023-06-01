from Engine.Input import Input
from Engine.GUIElement import Element
from Engine.Logging import Logging


class Textbox(Element):
    """[GUI] Текстовое поле"""
    
    def __init__(self, screen, style, x, y, text="", enable=True, maxLength=0, alphabet="123457890"):
        """Коснтруктор\nПринимает: (Window) screen - окно в котором необходимо рисовать, (Style) style - стиль, (int) x - коорината x, (int) y - координата y, (string) text - текст, (bool) enable - состояние, (int) maxLength - максимальная длина текста, (string) alphabet - алфавит доступных для ввода символов"""
        super().__init__(screen, style, x, y, text, enable)
        self.value = ""
        self.maxLength = maxLength
        self.selected = False
        self.alphabet = alphabet

    def __str__(self):
        """Возвращает текст из текствого поля\nВозвращает: (string) - текст из текствого поля"""
        return self.value
        
    def click(self, obj):
        """Событие нажатия"""
        if self.focused:
            self.selected = not(self.selected)
            if self.selected:
                self.select(self)

    def block(self):
        """Блокировка текстового поля"""
        self.focused = False
        self.enable = False
        self.selected = False

    def inputFromEvent(self,):
        """Обработка нажатий клавиатуры\nПринимает: (Event) event - событие"""
        if not(self.selected): return
        if Input.eventType == Input.Types.Keyboard:
            if Input.keyboardState == Input.Keyboard.DOWN and not Input.prevKeyboardState:
                if Input.keyboardCode == Input.Keyboard.Keys.BACKSPACE:
                    self.value = self.value[:-1]

                elif len(self.value) < self.maxLength or self.maxLength == 0:
                    if Input.keyboardChar in self.alphabet:
                        self.value += str(Input.keyboardChar)
                        self.change(self)

    def draw(self):
        """Отрисовка"""
        text = self.text + ": " + self.value
        self.intersectionLen = len(text)

        if self.enable:
            if self.selected:
                self.screen.text(text, self.x, self.y, wordPrefix=self.style["backgroundF"] + self.style["textF"])
            else:
                self.screen.text(text, self.x, self.y, wordPrefix=self.style["background"] + self.style["text"])
        else:
            self.screen.text(text, self.x, self.y, wordPrefix=self.style["disable"] + self.style["text"])