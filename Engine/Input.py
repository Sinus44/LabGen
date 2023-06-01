import ctypes
from ctypes.wintypes import *

# CTYPES ADAPTATE -------------------------------

#KEYBOARD
class CHAR_UNION(ctypes.Union):
    _fields_ = [("UnicodeChar", WCHAR),
                ("AsciiChar", CHAR)]

class KEY_EVENT_RECORD(ctypes.Structure):
    _fields_ = [("bKeyDown", BYTE),
                ("pad2", BYTE),
                ('pad1', SHORT),
                ("wRepeatCount", SHORT),
                ("wVirtualKeyCode", SHORT),
                ("wVirtualScanCode", SHORT),
                ("uChar", CHAR_UNION),
                ("dwControlKeyState", INT)]

#MOUSE
class MOUSE_EVENT_RECORD(ctypes.Structure):
    _fields_ = [("dwMousePosition", ctypes.wintypes._COORD),
                ("dwButtonState", INT),
                ("dwControlKeyState", INT),
                ("dwEventFlags", INT)]

#WINDOW BUFFER SIZE
class WINDOW_BUFFER_SIZE_RECORD(ctypes.Structure):
    _fields_ = [("dwSize", ctypes.wintypes._COORD)]

#MENU
class MENU_EVENT_RECORD(ctypes.Structure):
    _fields_ = [("dwCommandId", UINT)]

#FOCUS
class FOCUS_EVENT_RECORD(ctypes.Structure):
    _fields_ = [("bSetFocus", BYTE)]

#UNION
class INPUT_UNION(ctypes.Union):
    _fields_ = [("KeyEvent", KEY_EVENT_RECORD),
                ("MouseEvent", MOUSE_EVENT_RECORD),
                ("WindowBufferSizeEvent", WINDOW_BUFFER_SIZE_RECORD),
                ("MenuEvent", MENU_EVENT_RECORD),
                ("FocusEvent", FOCUS_EVENT_RECORD)]

#RECORD
class INPUT_RECORD(ctypes.Structure):
    _fields_ = [("EventType", SHORT),
                ("Event", INPUT_UNION)]

#RECORDS ARRAY
class INPUT_RECORD_ARRAY(ctypes.Structure):
	_fields_ = [("Records", INPUT_RECORD * 64)]

# -----------------------------------------------

class Input:
	"""Обработка входящих событий окна консоли"""

	EVENTS = []

	spec = " _+=-!@#$%^&*()<>.,~`|/\{}[];:'"
	numbers = "1234567890"
	
	angCaps = "QWERTYUIOPASDFGHJKLZXCVBNM"
	ang = angCaps.lower()

	ruCaps = "ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
	ru = ruCaps.lower()

	class Types:
		"""Типы событий"""
		Keyboard = 1
		Mouse = 2
		Window = 4
		Menu = 8
		Focus = 16

	class Mouse:
		"""События мыши"""
		#Mouse type:
		DOWN = 0
		MOVE = 1
		DOUBLECLICK = 2
		WHEELV = 4
		WHEELH = 8

		#Mouse key:
		NULL = 0
		LEFT = 1
		RIGHT = 2

	class Keyboard:
		"""События клавиатуры"""

		class Keys:
			"""Коды клавиш клавиатуры"""
			F1 = 112
			F2 = 113
			F3 = 114
			F4 = 115
			F5 = 116
			F6 = 117
			F7 = 118
			F8 = 119
			F9 = 120
			F10 = 121
			F11 = 122
			F12 = 123

			SPACE = 32
			BACKSPACE = 8
			TAB = 9
			ENTER = 13
			SHIFT = 16
			CTRL = 17
			ALT = 18
			CAPS = 20
			ESC = 27
			INSERT = 45
			PAGEUP = 33
			PAGEDOWN = 34
			END = 35
			HOME = 36
			DELETE = 46
			PRTSC = 44
			SCROLLLOCK = 145

			WINL = 91
			WINR = 92

			LEFT = 37
			UP = 38
			RIGHT = 39
			DOWN = 40

		DOWN = 1
		UP = 0

	class Window:
		"""События окна"""
		pass

	class Menu:
		"""События меню"""
		pass

	class Focus:
		"""События фокуса"""
		pass

	def init(useHotkey=False, lineInput=False, echo=False, resizeEvents=False, mouseEvents=False, insert=False, quickEdit=False, extended=False, handle=None):
		"""Включает получение событий\nПринимает: (bool) useHotkey - использование горячих клавиш, (bool) lineInput - описание отсутствует, (bool) echo - добавление в выходной массив, (bool) resizeEvents - принятие событий изменения размеров окна, (bool) mouseEvents - принятие событий мыши, (bool) insert - включает insert, (bool) quickEdit - выделение мышью, (bool) extended - запрет quickEdit"""
		Input.handle = handle or ctypes.windll.kernel32.GetStdHandle(-10)
		Input.events = ctypes.wintypes.DWORD()
		Input.record = (INPUT_RECORD * 8)()
		
		out = 0

		if useHotkey: out += 1
		if lineInput: out += 2
		if echo: out += 4
		if resizeEvents: out += 8
		if mouseEvents: out += 16
		if insert: out += 32
		if quickEdit: out += 64
		if extended: out += 128

		Input.varInit()

		ctypes.windll.kernel32.SetConsoleMode(Input.handle, out)

	def reset():
		"""Отчистка входного буффера"""
		
		# Получаем события
		Input.tick()

		# Если кол-во принятых событий не равно 0 то принимаем еще
		while Input.eventsRecived != False: 
			Input.tick()

		# Присваиваем переменным стандартные значения
		Input.varInit()
	
	def varInit():
		"""Сброс / инициализация переменных"""
		Input.event = 0
		Input.eventType = 0

		Input.mouseX = 0
		Input.mouseY = 0
		Input.mouseKey = 0
		Input.prevMouseState = False
		Input.mouseType = 0

		Input.keyboardCode = 0
		Input.keyboardChar = 0
		Input.keyboardState = 0
		Input.prevKeyboardState = False

	def tick():
		"""Получение и запись событий"""

		# Принимаем события от консоли
		ctypes.windll.kernel32.ReadConsoleInputExW(Input.handle, ctypes.byref(Input.record), 8, ctypes.byref(Input.events), 2)

		Input.event_count = int(bytes(Input.events)[0])
		Input.available = bool(Input.event_count)

		events_list = []
		for i in range(Input.event_count):
			event_dict = {}
			event_record = Input.record[i]
			event_type = event_record.EventType 
			event = event_record.Event
			event_dict["event"] = event
			event_dict["event_type"] = event_type
			event_dict["event_record"] = event_record

			event_dict["mouse_x"] = event.MouseEvent.dwMousePosition.X
			event_dict["mouse_y"] = event.MouseEvent.dwMousePosition.Y
			event_dict["mouse_key"] = event.MouseEvent.dwButtonState

			event_dict["key_code"] = event.KeyEvent.wVirtualKeyCode # Код кнопки клавиатуры
		

			events_list.append(event_dict)

		Input.events_list = events_list
		
		#Input.mouseType = Input.event.MouseEvent.dwEventFlags # колесо / нажатие / движение / двойное нажатие

		#Input.prevKeyboardState = Input.keyboardState if Input.eventType == Input.Types.Keyboard else False
		#Input.keyboardCode = Input.event.KeyEvent.wVirtualKeyCode # Код кнопки клавиатуры
		#Input.keyboardChar = Input.event.KeyEvent.uChar.UnicodeChar # Символ клавиши
		#Input.keyboardState = Input.event.KeyEvent.bKeyDown if Input.eventType == Input.Types.Keyboard else False # Состояние кнопки