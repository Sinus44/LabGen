from Engine.Input import Input
from Engine.GUIEvents import Events

class Element(Events):
    """[GUI] База для GUI элементов"""
    
    def __init__(self, screen=None, style=None, x=0, y=0, text="", enable=True, visible=True, root=None):
        """Коснтруктор\nПринимает: (Window) screen - окно в котором необходимо рисовать, (Style) style - стиль, (int) x - коорината x, (int) y - координата y, (string) text - текст, (bool) enable - состояние, (bool) visible - отрисовывать ли элемент"""
        self.screen = screen
        self.style = style
        self.x = x
        self.y = y
        self.text = text
        self.root = root
        self.focused = False
        self.intersectionLen = len(text)
        self.enable = enable
        self.visible = visible

    def block(self):
        """Блокировка элемента"""
        self.focused = False
        self.enable = False

    def intersectionFromEvent(self):
        """Проверка на пересечение с мышью из события\n(Event) - событие"""
        if self.enable:
            if Input.eventType == Input.Types.Mouse:
                if Input.mouseType == Input.Mouse.MOVE:
                    self.intersection(Input.mouseX, Input.mouseY)

    def intersection(self, x, y):
        """Проверка на пересечение по координатам\nПринимает: (int) x - координата x, (int) y - координата y"""
        if self.enable:
            if (self.x <= x < self.x + self.intersectionLen) and (self.y == y):
                self.focused = True
                self.focus(self)
            else:
                self.focused = False
