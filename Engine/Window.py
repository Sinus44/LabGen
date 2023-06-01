import ctypes
import os

class Window:
	"""Изображение в консоли"""

	def __init__(self, console:object):
		"""Принимает консоль с которой необходимо взаимодействовать"""
		self.console = console
		self.size = console.get_size()
		self.w = self.size[0]
		self.h = self.size[1]
		self.buffer = [[]]

	def print(self) -> None:
		"""Вывод буффера в консоль"""
		s = ""
		for string in self.buffer:
			s = s +"".join(string)

		self.console.print(s)

	def clear(self) -> None:
		"""Отчистка вывода в консоль"""
		os.system("cls")

	def fill(self, symbol:str=" "):
		"""Заливка всего буффера определенным символом"""
		symbol = str(symbol)
		self.buffer = []
		for i in range(self.h):
			self.buffer.append([])
			for j in range(self.w):
				self.buffer[i].append(symbol)

	def point(self, x:int, y:int, symbol:int="*"):
		"""Установка символа в буффер по координатам\nПринимает: (int) x - координата x, (int) y - координата y, (string) symbol - символ для заливки"""
		if (0 <= x < self.w) and (0 <= y < self.h):
				self.buffer[y][x] = symbol

	def rectFill(self, x:int=0, y:int=0, w:int=1, h:int=1, symbol:str="*"):
		"""Заполненный прямоугольник в буффер\nПринимает: (int) x - координата x, (int) y - координата y, (int) w - ширина, (int) h - высота, (string) symbol - символ для заливки"""
		for i in range(h):
			for j in range(w):
				self.point(j+x, i+y, symbol)
				#self.buffer[i+y][j+x] = symbol

	def rect(self, x:int=0, y:int=0, w:int=1, h:int=1, symbol:str="*"):
		"""Пустотелый прямоугольник в буффер\nПринимает: (int) x - координата x, (int) y - координата y, (int) w - ширина, (int) h - высота, (string) symbol - символ для заливки"""
		for i in range(h):
			for j in range(w):
				if i == 0 or i == h-1 or j == 0 or j == w - 1:
					self.point(j + x, i + y, symbol)

	def circleFill(self, x:int=0, y:int=0, r:int=1, symbol:str="*"):
		"""Залитый круг в буффер\nПринимает: (int) x - координата x, (int) y - координата y, (int) r - радиус, (string) symbol - символ для заливки"""
		for i in range(self.h):
			for j in range(self.w):
				if (i - y) ** 2 + (j - x) **2  <= r ** 2:
					self.buffer[i][j] = symbol

	def circle(self, x=0, y=0, r=1, symbol="*"):
		"""Пустотелый круг в буффер\nПринимает: (int) x - координата x, (int) y - координата y, (int) r - радиус, (string) symbol - символ для заливки"""
		disp_x = x
		disp_y = y
		x = 0
		y = r
		delta = (1 - 2 * r)
		error = 0
		while y >= 0:
			self.point(disp_x + x, disp_y + y, symbol)
			self.point(disp_x + x, disp_y - y, symbol)
			self.point(disp_x - x, disp_y + y, symbol)
			self.point(disp_x - x, disp_y - y, symbol)

			error = 2 * (delta + y) - 1
			if ((delta < 0) and (error <=0)):
				x+=1
				delta = delta + (2*x+1)
				continue
			error = 2 * (delta - x) - 1
			if ((delta > 0) and (error > 0)):
				y -= 1
				delta = delta + (1 - 2 * y)
				continue
			x += 1
			delta = delta + (2 * (x - y))
			y -= 1

	def line(self, x1=0, y1=0, x2=0, y2=0, symbol="*"):
		"""Линия по координатам\nПринимает: (int) x1 - координата x1, (int) y1 - координата y1, (int) x2 - координата x2, (int) y2 - координата y2, (string) symbol - символ для заливки"""
		delX = abs(x2 - x1)
		delY = abs(y2 - y1)

		signX, signY = 0, 0

		if x1 < x2: signX = 1
		else: signX = -1

		if y1 < y2: signY = 1
		else: signY = -1

		error = delX - delY
		self.point(x2, y2, symbol)

		while (x1 != x2 or y1 != y2): 
			self.point(x1, y1, symbol)
			error_2 = error * 2
		
			if error_2 > -delY: 
				error -= delY
				x1 += signX
		
			if error_2 < delX:
				error += delX
				y1 += signY

	def paste(self, window, x=0, y=0):
		"""Вставка буффера другого объекта в текущий\nПринимает: (Window) - Окно из которого копировать, (int) x - кооридната x, (int) y - коорината y"""
		if x + window.w > self.w or y + window.h > self.h:
			return

		for i in range(len(window.buffer)):
			for j in range(len(window.buffer[0])):
				if window.buffer[i][j] == 0:
					continue
				self.buffer[i+y][j+x] = window.buffer[i][j]

	def text(self, x:int, y:int, text:str="TEXT", text_prefix:str="", symbol_prefix:str="", text_postfix:str="", symbol_postfix:str=""):
		"""Текст\nПринимает: (string) text - текст, (int) x - кооридната x, (int) y - коорината y, (string) wordPrefix - префикс перед текстом, (string) symbolPrefix - префикс перед символом, (string) wordPostfix - постфикс после текста, (string) symbolPostfix - постфикс после символа"""
		if (x < 0 or y < 0) or (x + len(text) > self.w):
			return

		for i in range(len(text)):
			self.buffer[y][x+i] = (text_prefix if i == 0 else "") + symbol_prefix + text[i] + symbol_postfix + (text_postfix if i == len(text) - 1 else "")