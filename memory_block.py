from tkinter import *

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
		self.memAddress000 = Text(root, height = 3, width = 15, state = "normal", bg = consoleColor, font = entryFont, fg = "#05fa42")
		# self.memAddress000.insert(END, "test")
		self.memAddress000.grid(row = 2, column = 0, padx = 2, pady=2)

		self.memAddress001Label = Label(root, text = "001", bg = backGroundColor, font = entryFont, fg = "#03b6fc")
		self.memAddress001Label.grid(row = 1, column = 1)
		self.memAddress001 = Text(root, height = 3, width = 15, state = "disable", bg = consoleColor)
		self.memAddress001.grid(row = 2, column = 1, padx = 2, pady=2)

		self.memAddress010Label = Label(root, text = "010", bg = backGroundColor, font = entryFont, fg = "#03b6fc")
		self.memAddress010Label.grid(row = 1, column = 2)
		self.memAddress010 = Text(root, height = 3, width = 15, state = "disable", bg = consoleColor)
		self.memAddress010.grid(row = 2, column = 2, padx = 2, pady=2)

		self.memAddress011Label = Label(root, text = "011", bg = backGroundColor, font = entryFont, fg = "#03b6fc")
		self.memAddress011Label.grid(row = 1, column = 3)
		self.memAddress011 = Text(root, height = 3, width = 15, state = "disable", bg = consoleColor)
		self.memAddress011.grid(row = 2, column = 3, padx = 2, pady=2)

		self.memAddress100Label = Label(root, text = "100", bg = backGroundColor, font = entryFont, fg = "#03b6fc")
		self.memAddress100Label.grid(row = 1, column = 4)
		self.memAddress100 = Text(root, height = 3, width = 15, state = "disable", bg = consoleColor)
		self.memAddress100.grid(row = 2, column = 4, padx = 2, pady=2)

		self.memAddress101Label = Label(root, text = "101", bg = backGroundColor, font = entryFont, fg = "#03b6fc")
		self.memAddress101Label.grid(row = 1, column = 5)
		self.memAddress101 = Text(root, height = 3, width = 15, state = "disable", bg = consoleColor)
		self.memAddress101.grid(row = 2, column = 5, padx = 2, pady=2)

		self.memAddress110Label = Label(root, text = "110", bg = backGroundColor, font = entryFont, fg = "#03b6fc")
		self.memAddress110Label.grid(row = 1, column = 6)
		self.memAddress110 = Text(root, height = 3, width = 15, state = "disable", bg = consoleColor)
		self.memAddress110.grid(row = 2, column = 6, padx = 2, pady=2)

		self.memAddress111Label = Label(root, text = "111", bg = backGroundColor, font = entryFont, fg = "#03b6fc")
		self.memAddress111Label.grid(row = 1, column = 7)
		self.memAddress111 = Text(root, height = 3, width = 15, state = "disable", bg = consoleColor)
		self.memAddress111.grid(row = 2, column = 7, padx = 2, pady=2)