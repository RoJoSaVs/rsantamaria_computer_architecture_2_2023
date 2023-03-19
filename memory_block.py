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
		self.memAddress000 = Text(root, height = 3, width = 15, state = "normal", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.memAddress000.insert(END, "test")
		self.memAddress000.grid(row = 1, column = 0, padx = 2, pady=2)

		self.memAddress001 = Text(root, height = 3, width = 15, state = "disable", bg = consoleColor)
		self.memAddress001.grid(row = 1, column = 1, padx = 2, pady=2)

		self.memAddress010 = Text(root, height = 3, width = 15, state = "disable", bg = consoleColor)
		self.memAddress010.grid(row = 1, column = 2, padx = 2, pady=2)

		self.memAddress011 = Text(root, height = 3, width = 15, state = "disable", bg = consoleColor)
		self.memAddress011.grid(row = 1, column = 3, padx = 2, pady=2)

		self.memAddress100 = Text(root, height = 3, width = 15, state = "disable", bg = consoleColor)
		self.memAddress100.grid(row = 1, column = 4, padx = 2, pady=2)

		self.memAddress101 = Text(root, height = 3, width = 15, state = "disable", bg = consoleColor)
		self.memAddress101.grid(row = 1, column = 5, padx = 2, pady=2)

		self.memAddress110 = Text(root, height = 3, width = 15, state = "disable", bg = consoleColor)
		self.memAddress110.grid(row = 1, column = 6, padx = 2, pady=2)

		self.memAddress111 = Text(root, height = 3, width = 15, state = "disable", bg = consoleColor)
		self.memAddress111.grid(row = 1, column = 7, padx = 2, pady=2)