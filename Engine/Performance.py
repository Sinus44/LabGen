import time
import timeit

class Performance:
	"""Замер времени выполнения кода"""
	
	startTime = 0
	
	def start():
		"""Указывает начальное время отсчета"""
		Performance.startTime = time.time()
	
	def time():
		"""Возвращает время прошедшее с точки отсчета\nВозвращает: (float) - время в секундах"""
		return time.time() - Performance.startTime

	def function(f, repeats=1, count=1):
		"""Возвращает время выполнения функции\nПринимает: (function) f - функция для тестирования, (int) repeats - кол-во повторений 1го замера, (int) count - кол-во замеров\nВозвращает: (float) - время в секундах"""
		return timeit.repeat(f, repeat=repeats, number=count)