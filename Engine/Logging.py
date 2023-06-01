import datetime

class Logging:
	"""Запись отладочной информации в файл"""

	def log(*text):
		"""Логирование в файл\nПринимает: (*strings) - строки для логгирования"""
		date = datetime.datetime.now()
		file = open(f"{date.day}{date.month}{date.year}.log", "a")

		for i in text:
			i = str(i)
			file.write(f"[{'{:2.0f}'.format(date.hour)}:{'{:2.0f}'.format(date.minute)}:{'{:2.0f}'.format(date.second)}]: {str(i)}\n")

		file.close()

	def print(*text, end="\n"):
		"""Логирование в консольnПринимает: (*strings) - строки для логгирования"""
		date = datetime.datetime.now()
		
		for i in text:
			i = str(i)
			print(f"[{'{:2.0f}'.format(date.hour)}:{'{:2.0f}'.format(date.minute)}:{'{:2.0f}'.format(date.second)}]: {str(i)}", end=end)
