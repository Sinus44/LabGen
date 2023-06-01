from Engine.GUIElement import Element

class Button(Element):
	"""[GUI] Кнопка"""
	
	def draw(self):
		"""Отрисовка"""
		text = f"[ {self.text} ]"
		self.intersectionLen = len(text)

		if self.enable:
			if self.focused:
				self.screen.text(text, self.x, self.y, wordPrefix=self.style["backgroundF"] + self.style["textF"])
			else:
				self.screen.text(text, self.x, self.y, wordPrefix=self.style["background"] + self.style["text"])
		else:
			self.screen.text(text, self.x, self.y, wordPrefix=self.style["disable"] + self.style["text"])