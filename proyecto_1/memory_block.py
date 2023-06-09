from tkinter import *
from constants import *

ownFont = ("Comic Sans MS", 12)
entryFont = ("Comic Sans MS", 10)
backGroundColor = "#1a1a1a"
consoleColor = "black"


class MemoryBlock():
	def __init__(self, root):
		self.memoryLabel = Label(root, text = "Memory", bg = backGroundColor, font = ownFont, fg = "#03b6fc")
		self.memoryLabel.grid(row = 0, column = 0, columnspan = 8)

		# self.memAddress000 = Text(root, height = 3, width = 15, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		# https://stackoverflow.com/questions/3842155/is-there-a-way-to-make-the-tkinter-text-widget-read-only

		self.memAddress000Label = Label(root, text = "000", bg = backGroundColor, font = entryFont, fg = "#03b6fc")
		self.memAddress000Label.grid(row = 1, column = 0)
		self.memAddress000 = Text(root, height = 3, width = 15, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.memAddress000.grid(row = 2, column = 0, padx = 2, pady=2)

		self.memAddress001Label = Label(root, text = "001", bg = backGroundColor, font = entryFont, fg = "#03b6fc")
		self.memAddress001Label.grid(row = 1, column = 1)
		self.memAddress001 = Text(root, height = 3, width = 15, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.memAddress001.grid(row = 2, column = 1, padx = 2, pady=2)

		self.memAddress010Label = Label(root, text = "010", bg = backGroundColor, font = entryFont, fg = "#03b6fc")
		self.memAddress010Label.grid(row = 1, column = 2)
		self.memAddress010 = Text(root, height = 3, width = 15, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.memAddress010.grid(row = 2, column = 2, padx = 2, pady=2)

		self.memAddress011Label = Label(root, text = "011", bg = backGroundColor, font = entryFont, fg = "#03b6fc")
		self.memAddress011Label.grid(row = 1, column = 3)
		self.memAddress011 = Text(root, height = 3, width = 15, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.memAddress011.grid(row = 2, column = 3, padx = 2, pady=2)

		self.memAddress100Label = Label(root, text = "100", bg = backGroundColor, font = entryFont, fg = "#03b6fc")
		self.memAddress100Label.grid(row = 1, column = 4)
		self.memAddress100 = Text(root, height = 3, width = 15, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.memAddress100.grid(row = 2, column = 4, padx = 2, pady=2)

		self.memAddress101Label = Label(root, text = "101", bg = backGroundColor, font = entryFont, fg = "#03b6fc")
		self.memAddress101Label.grid(row = 1, column = 5)
		self.memAddress101 = Text(root, height = 3, width = 15, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.memAddress101.grid(row = 2, column = 5, padx = 2, pady=2)

		self.memAddress110Label = Label(root, text = "110", bg = backGroundColor, font = entryFont, fg = "#03b6fc")
		self.memAddress110Label.grid(row = 1, column = 6)
		self.memAddress110 = Text(root, height = 3, width = 15, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.memAddress110.grid(row = 2, column = 6, padx = 2, pady=2)

		self.memAddress111Label = Label(root, text = "111", bg = backGroundColor, font = entryFont, fg = "#03b6fc")
		self.memAddress111Label.grid(row = 1, column = 7)
		self.memAddress111 = Text(root, height = 3, width = 15, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.memAddress111.grid(row = 2, column = 7, padx = 2, pady=2)


	def startMemory(self):
		self.memAddress000.config(state = NORMAL)
		self.memAddress000.insert(END, "0000")
		self.memAddress000.config(state = DISABLED)

		self.memAddress001.config(state = NORMAL)
		self.memAddress001.insert(END, "0000")
		self.memAddress001.config(state = DISABLED)

		self.memAddress010.config(state = NORMAL)
		self.memAddress010.insert(END, "0000")
		self.memAddress010.config(state = DISABLED)

		self.memAddress011.config(state = NORMAL)
		self.memAddress011.insert(END, "0000")
		self.memAddress011.config(state = DISABLED)

		self.memAddress100.config(state = NORMAL)
		self.memAddress100.insert(END, "0000")
		self.memAddress100.config(state = DISABLED)

		self.memAddress101.config(state = NORMAL)
		self.memAddress101.insert(END, "0000")
		self.memAddress101.config(state = DISABLED)

		self.memAddress110.config(state = NORMAL)
		self.memAddress110.insert(END, "0000")
		self.memAddress110.config(state = DISABLED)

		self.memAddress111.config(state = NORMAL)
		self.memAddress111.insert(END, "0000")
		self.memAddress111.config(state = DISABLED)


	def setRamValue(self, value, memAddress):
		if(memAddress == 0):
			ramModelVector[0] = value
			self.memAddress000.config(state = NORMAL)
			self.memAddress000.delete("1.0", END)
			self.memAddress000.insert(END, ramModelVector[0])
			self.memAddress000.config(state = DISABLED)

		elif(memAddress == 1):
			ramModelVector[1] = value
			self.memAddress001.config(state = NORMAL)
			self.memAddress001.delete("1.0", END)
			self.memAddress001.insert(END, ramModelVector[1])
			self.memAddress001.config(state = DISABLED)

		elif(memAddress == 2):
			ramModelVector[2] = value
			self.memAddress010.config(state = NORMAL)
			self.memAddress010.delete("1.0", END)
			self.memAddress010.insert(END, ramModelVector[2])
			self.memAddress010.config(state = DISABLED)

		elif(memAddress == 3):
			ramModelVector[3] = value
			self.memAddress011.config(state = NORMAL)
			self.memAddress011.delete("1.0", END)
			self.memAddress011.insert(END, ramModelVector[3])
			self.memAddress011.config(state = DISABLED)

		elif(memAddress == 4):
			ramModelVector[4] = value
			self.memAddress100.config(state = NORMAL)
			self.memAddress100.delete("1.0", END)
			self.memAddress100.insert(END, ramModelVector[4])
			self.memAddress100.config(state = DISABLED)
			
		elif(memAddress == 5):
			ramModelVector[5] = value
			self.memAddress101.config(state = NORMAL)
			self.memAddress101.delete("1.0", END)
			self.memAddress101.insert(END, ramModelVector[5])
			self.memAddress101.config(state = DISABLED)
			
		elif(memAddress == 6):
			ramModelVector[6] = value
			self.memAddress110.config(state = NORMAL)
			self.memAddress110.delete("1.0", END)
			self.memAddress110.insert(END, ramModelVector[6])
			self.memAddress110.config(state = DISABLED)
			
		elif(memAddress == 7):
			ramModelVector[7] = value
			self.memAddress111.config(state = NORMAL)
			self.memAddress111.delete("1.0", END)
			self.memAddress111.insert(END, ramModelVector[7])
			self.memAddress111.config(state = DISABLED)


	def updateRamValue(self):
		self.memAddress000.config(state = NORMAL)
		self.memAddress000.delete("1.0", END)
		self.memAddress000.insert(END, ramModelVector[0])
		self.memAddress000.config(state = DISABLED)

		self.memAddress001.config(state = NORMAL)
		self.memAddress001.delete("1.0", END)
		self.memAddress001.insert(END, ramModelVector[1])
		self.memAddress001.config(state = DISABLED)

		self.memAddress010.config(state = NORMAL)
		self.memAddress010.delete("1.0", END)
		self.memAddress010.insert(END, ramModelVector[2])
		self.memAddress010.config(state = DISABLED)

		self.memAddress011.config(state = NORMAL)
		self.memAddress011.delete("1.0", END)
		self.memAddress011.insert(END, ramModelVector[3])
		self.memAddress011.config(state = DISABLED)

		self.memAddress100.config(state = NORMAL)
		self.memAddress100.delete("1.0", END)
		self.memAddress100.insert(END, ramModelVector[4])
		self.memAddress100.config(state = DISABLED)
			
		self.memAddress101.config(state = NORMAL)
		self.memAddress101.delete("1.0", END)
		self.memAddress101.insert(END, ramModelVector[5])
		self.memAddress101.config(state = DISABLED)
			
		self.memAddress110.config(state = NORMAL)
		self.memAddress110.delete("1.0", END)
		self.memAddress110.insert(END, ramModelVector[6])
		self.memAddress110.config(state = DISABLED)
			
		self.memAddress111.config(state = NORMAL)
		self.memAddress111.delete("1.0", END)
		self.memAddress111.insert(END, ramModelVector[7])
		self.memAddress111.config(state = DISABLED)
