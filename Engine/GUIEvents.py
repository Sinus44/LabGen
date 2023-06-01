class Events:
    """[GUI] Шаблоны событий для GUI элементов"""
    
    def click(self, obj):
        """Нажатие\nПринимает: (object) obj - инициатор события"""
        pass

    def change(self, obj):
        """Изменение состояние\nПринимает: (object) obj - инициатор события"""
        pass

    def focus(self, obj):
        """Наведение мышью на элемент\nПринимает: (object) obj - инициатор события"""
        pass

    def select(self, obj):
        """Выбор элемента\nПринимает: (object) obj - инициатор события"""
        pass