from Engine.Logging import Logging

class Group:
    """[GUI] Группа GUI элементов"""

    def __init__(self, screen, x, y, interval=1, maxElements=10):
        """Конструктор\nПринимает: (Winow) screen - окно для отрисовки, (int) x - кооридната x, (int) y - координата y, (int) interval - интервал между элементами, (int) maxElements - максимальное кол-во элеметов для отрисовки"""
        self.screen = screen
        self.x = x
        self.y = y
        self.elements = []
        self.interval = interval
        self.selected = {}
        self.maxElements = maxElements

    def append(self, element):
        """Добавление элементов в группу\nПринимает: (Element or any [GUI]) element - элемент для добавления в группу"""
        self.elements.append(element)
    
    def eventHandler(self):
        """Обработка событий для всех элементов в группе\nПринимает: (Event) - событие"""
        for element in self.elements:
            element.intersectionFromEvent()

            if hasattr(element, "inputFromEvent"):
                element.inputFromEvent()
    
    def click(self):
        """Обработка событий для всех элементов в группе"""
        for element in self.elements:
            if element.focused:
                element.click(element)
    
    def sort(self):
        """Автопозиционирование элементов группы"""
        for i in range(len(self.elements)):
            element = self.elements[i]
            element.x = self.x
            element.y = self.y + i * (self.interval + 1)

    def draw(self):
        """Отрисовка всех элементов группы"""
        for i in range(min(len(self.elements), self.maxElements)):
            self.elements[i].draw()