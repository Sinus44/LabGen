class Color:
	"""Работа с цветами для консоли"""

	default = "\33[0m"
	underline = "\33[4m"
	negative = "\33[7m"

	def rgb_background(r:int=0, g:int=0, b:int=0) -> str:
		"""Возвращает символ-код установки цвета фона"""
		return f"\33[48;2;{r};{g};{b}m"

	def rgb_text(r:int=0, g:int=0, b:int=0) -> str:
		"""Возвращает символ-код установки цвета основного текста"""
		return f"\33[38;2;{r};{g};{b}m"