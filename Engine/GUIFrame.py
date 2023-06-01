class Frame:
	"""[GUI] Фона"""
	
	def __init__(self):
		"""[GUI] Фон """
		self.root = None
		self.style = None
	
	def draw(self):
		"""Отрисовка"""
		self.screen.fill(self.style["background"] + " ")