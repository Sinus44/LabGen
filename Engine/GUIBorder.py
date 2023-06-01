from Engine.GUIStyle import Style

class Border:
	"""[GUI] Рамка для изображения"""
	
	def __init__(self, screen, style, symbol="*"):
		"""Конструктор\nПринимает: (Window) screen - окно в котором необдимо рисовать, (Style) style - стиль, (string) symbol - символ"""
		self.screen = screen
		self.style = style
		self.symbol = symbol
		
	def draw(self):
		"""Отрисовка"""
		self.screen.rect(0, 0, self.screen.w, self.screen.h, self.style["text"] + self.style["background"] + self.symbol)