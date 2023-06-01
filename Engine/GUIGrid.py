

class Grid:
    """[GUI] Визуальная сетка"""

    def __init__(self, screen, x, y, w, h, columns, strings, style):
        """Коструктор\nПринимает: (Window) screen - окно для отрисовки, (int) x - координата x, (int) y - координата y, (int) w - ширина, (int) h - высота, (int) columns - кол-во столбцов, (int) strings - кол-во строк, (Style) style - стиль"""
        self.screen = screen
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.columns = columns
        self.strings = strings
        self.style = style

        self.cellW = (w - (columns - 1)) // columns
        self.cellH = (h - (strings - 1)) // strings
    
    def intersection(self, x, y):
        """Вовзращает координаты в сетке\nПринимает: (int) x - координата x, (int) y - координата y\nВозвращает: (tuple_int) - координаты ячейки по которой нажали"""
        x1 = x // self.cellW
        y1 = y // self.cellH
        return (x1, y1)
    
    def draw(self):
        """Отрисовка"""
        for i in range(1, self.columns):
            self.screen.line(self.x + i * self.cellW, self.y, self.x + i * self.cellW, self.y + self.h, self.style["background"] + self.style["text"] + "|")
        
        for i in range(1, self.strings):
            self.screen.line(self.x, self.y + i * self.cellH, self.x + self.w, self.y + i * self.cellH, self.style["background"] + self.style["text"] + "-")