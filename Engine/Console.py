import ctypes
import sys
import os
import ctypes.wintypes
import threading
import time
import win32file
import win32pipe
import random

class CONSOLE_SCREEN_BUFFER_INFO(ctypes.Structure):
    _fields_ = [
        ("dwSize", ctypes.wintypes._COORD),
        ("dwCursorPosition", ctypes.wintypes._COORD),
        ("wAttributes", ctypes.wintypes.WORD),
        ("srWindow", ctypes.wintypes.SMALL_RECT),
        ("dwMaximumWindowSize", ctypes.wintypes._COORD),
    ]

class Console:
	def __init__(self):
		self.id = random.randint(1000, 9999)
		self.pipe_out_name = r"\\.\pipe\consoleout" + str(self.id)
		self.pipe_in_name = r"\\.\pipe\consolein" + str(self.id)
		self.enable = False

		self.pipe_in = win32pipe.CreateNamedPipe(
			self.pipe_in_name,
			win32pipe.PIPE_ACCESS_DUPLEX,
			win32pipe.PIPE_TYPE_MESSAGE | win32pipe.PIPE_WAIT,
			1,
			65536,
			65536,
			0,
			None
		)

		threading.Thread(target=os.system, args=[f"start py ./engine/sub_console.py {self.id}"], daemon=False).start()
		time.sleep(1)

		try:
			self.pipe_out = win32file.CreateFile(
				self.pipe_out_name,
				win32file.GENERIC_READ | win32file.GENERIC_WRITE,
				0, None,
				win32file.OPEN_EXISTING,
				0, None
			)
			self.enable = True
		except:
			print(f"[ERROR][Console] Не удалось соединится с консолью")
			self.pipe_out = None
			self.enable = False

	def send(self, data):
		if not self.enable: return
		try:
			win32file.WriteFile(self.pipe_out, data)
		except:
			self.enable = False

	def print(self, data):
		request = ((2).to_bytes(1, "little")) + data.encode()
		self.send(request)

	def set_size(self, w:int, h:int):
		if w > 255 or h > 255: return
		request = ((5).to_bytes(1, "little")) + ((w).to_bytes(1, "little")) + ((h).to_bytes(1, "little"))
		self.send(request)
		time.sleep(1)

	def set_title(self, title:str):
		request = ((3).to_bytes(1, "little")) + title.encode()
		self.send(request)
		time.sleep(0.01)

	def set_icon(self, path:str):
		request = ((4).to_bytes(1, "little")) + path.encode()
		self.send(request)

	def close(self):
		if not self.enable: return
		request = (1).to_bytes(1, "little")
		self.send(request)
		self.enable = False

	def get_size(self):
		request = ((6).to_bytes(1, "little"))
		self.send(request)
		time.sleep(1)
		res = win32file.ReadFile(self.pipe_in, 4096)
		if int(res[1][0]) == 1:
			return (int(res[1][1]), int(res[1][2]))
		else:
			return (0, 0)

	def __del__(self):
		self.close()

class Root_Console:
	def __init__(self):
		...

	def print(self, data:str):
		print(data, end="")

	def change_title(self, title:str):
		ctypes.windll.kernel32.SetConsoleTitleW(title)

	def change_size(self, w:int, h:int):
		os.system(f'mode con cols={w} lines={h}')

	def change_icon(self, path:str):
		hwnd = ctypes.windll.kernel32.GetConsoleWindow()
		icon_handle = ctypes.windll.user32.LoadImageW(None, path, 1, 0, 0, 16)
		ctypes.windll.user32.SendMessageW(hwnd, 0x80, 0, icon_handle)

	def get_size(self):
		csbi = CONSOLE_SCREEN_BUFFER_INFO()
		ctypes.windll.kernel32.GetConsoleScreenBufferInfo(ctypes.windll.kernel32.GetStdHandle(-11), ctypes.byref(csbi))

		width = csbi.srWindow.Right - csbi.srWindow.Left + 1
		height = csbi.srWindow.Bottom - csbi.srWindow.Top + 1
		return (width, height)

	def set_size(self, w:int, h:int):
		if w > 255 or h > 255: return
		os.system(f'mode con cols={w} lines={h-1}')

	def close(self):
		...