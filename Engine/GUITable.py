from Engine.Input import Input
from Engine.Logging import Logging

class Table:
    """[GUI] Таблица"""
    
    def __init__(self, screen, style, x, y, w, h):
        """Конструктор\nПринимает: (Window) screen - окно для отрисовки, (Style) - стиль, (int) x - x координата, (int) y - y координата, (int) w - ширина, (int) h - высота"""
        self.screen = screen
        self.style = style
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.selected = 0
        self.strings = []
    
    def resize(self):
        """Перерасчет размеров таблицы"""
        if len(self.strings):
            self.columns = len(self.strings)
            self.columnsW = (self.w - (self.columns - 1)) // self.columns
        else:
            self.columns = 0
            self.columnsW = self.w

    def click(self, obj):
        """Нажатие\nПринимает: (object) obj - инициатор события"""
        if self.focused:
            self.selected = not(self.selected)
            if self.selected:
                self.select(self)

    def block(self):
        """Блокировка текстового поля"""
        self.focused = False
        self.enable = False
        self.selected = False

    def inputFromEvent(self, event):
        """Обработка нажатий клавиатуры\nПринимает: (Event) event - событие"""
        if not(self.selected): return
        if event.type == Input.Types.Keyboard:
            if event.keyboardState == Input.Keyboard.DOWN:
                if event.keyboardCode == Input.Keyboard.Keys.BACKSPACE:
                    self.value = self.value[:-1]

                elif len(self.value) < self.maxLength or self.maxLength == 0:
                    if event.keyboardChar in self.alphabet: # вот это
                        self.value += str(event.keyboardChar) # пофиксить
                        self.change(self)

    def draw(self):
        """Отрисовка"""

        for i in range(min(len(self.strings), (self.h // 2) + 1)):
            y = self.y + 1 + i * 2
            self.screen.line(self.x, y, self.x + self.w - 1, y, self.style["background"] + self.style["text"] + "*")

            for j in range(self.columns):
                x = self.x + (j * (self.columnsW + 1)) - 1
                if j:
                    self.screen.line(x, self.y, x, self.y + self.h, self.style["background"] + self.style["text"] + "*")
               
                if(len(self.strings)):
                    if(len(self.strings[0])):
                        self.screen.text(self.strings[j][i], x + 1, y - 1, wordPrefix=self.style["background"] + self.style["text"])