class Scene_Control:
	"""Управления отображаемыми сценами"""

	def __init__(self):
		self.scenes_list = {}
		self.selected = ""
		self.prev = ""

	def set(self, name:str) -> None:
		"""Установка сцены по имени"""
		self.prev = self.selected

		if self.prev:
			self.scenes_list[self.prev].remove()

		self.selected = name
		self.scenes_list[self.selected].select()

	def add(self, name:str, scene:object) -> None:
		"""Добавление сцены"""
		self.scenes_list[name] = scene

	def addFromDict(self, scenes:dict) -> None:
		"""Импорт сцен из словаря"""
		for scene in scenes:
			self.add(scene, scenes[scene])

	def play(self) -> None:
		"""Воспроизведение сцены"""
		self.scenes_list[self.selected].play()

class Scene:
	def __init__(self):
		...

	def remove(self):
		...

	def play(self):
		...

	def select(self):
		...