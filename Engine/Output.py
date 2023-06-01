import ctypes
import ctypes.wintypes
import os

class Output:
	"""Настройка выходного буффера окна консоли"""

	def init(handle:int, mode:int=5) -> bool:
		"""Иницаилизация окна консоли"""
		return bool(ctypes.windll.kernel32.SetConsoleMode(handle, mode))

	def get_title() -> str:
		"""Получение заголовка окна консоли"""
		out = (ctypes.c_char * 256)()
		size = ctypes.windll.kernel32.GetConsoleTitleW(ctypes.byref(out), ctypes.wintypes.DWORD(256))
		return bytes(out).decode("utf-16-le")[:size]
