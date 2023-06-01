from Engine import *
import time
import random

class Cell:
	def __init__(self, i, j, x, y):
		self.i = i
		self.j = j
		self.up = True
		self.down = True
		self.right = True
		self.left = True
		self.x = x
		self.y = y
		self.current = False
		self.checked = False

	def draw(self, w):
		w.rect(self.x, self.y, 3, 3, "|")

		if not self.up:
			w.point(self.x + 1, self.y, " ")

		if not self.down:
			w.point(self.x + 1, self.y + 2, " ")
		
		if not self.left:
			w.point(self.x, self.y + 1, " ")
		
		if not self.right:
			w.point(self.x + 2, self.y + 1, " ")

		if self.current:
			backcolor = Color.rgb_background(0,255,0)
		else:
			if self.checked:
				backcolor = Color.rgb_background(0,0,0)
			else:
				backcolor = Color.rgb_background(255,0,0)

		w.point(self.x+1,self.y+1, backcolor + " " + Color.default)

count = 20
cells = [[Cell(i, j, i * 3, j * 3) for j in range(count)] for i in range(count)]

c = Root_Console()
c.set_size(3 * count, 3 * count + 1)
w = Window(c)

i = 0

currentCell = cells[0][0]

def OnBoard(i, j):
	return 0 <= j < count and 0 <= i < count

path = [currentCell]

def CheckAll():
	for row in cells:
		for cell in row:
			if not cell.checked:
				return True
	return False

while CheckAll():
	time.sleep(1)
	w.fill()

	choise = []

	currentCell = path[-1]
	currentCell.checked = True

	if OnBoard(currentCell.i-1,currentCell.j):
		if not cells[currentCell.i-1][currentCell.j].checked:
			choise.append(cells[currentCell.i-1][currentCell.j])
	
	if OnBoard(currentCell.i,currentCell.j-1):
		if not cells[currentCell.i][currentCell.j-1].checked:
			choise.append(cells[currentCell.i][currentCell.j-1])
	
	if OnBoard(currentCell.i+1,currentCell.j):
		if not cells[currentCell.i+1][currentCell.j].checked:
			choise.append(cells[currentCell.i+1][currentCell.j])
	
	if OnBoard(currentCell.i,currentCell.j+1):
		if not cells[currentCell.i][currentCell.j+1].checked:
			choise.append(cells[currentCell.i][currentCell.j+1])

	for row in cells:
		for cell in row:
			cell.current = cell == currentCell
			cell.draw(w)
	
	if (len(choise) < 1):
		path.pop(-1)

	else:
		nextcell = random.choice(choise)
		dx = nextcell.i - currentCell.i
		dy = nextcell.j - currentCell.j

		if dy == -1:
			nextcell.down = False
			currentCell.up = False

		elif dy == 1:
			nextcell.up = False
			currentCell.down = False

		elif dx == -1:
			nextcell.right = False
			currentCell.left = False

		elif dx == 1:
			nextcell.left = False
			currentCell.right = False

		path.append(nextcell)

	w.print()

input()