from tkinter import *

ownFont = ("Comic Sans MS", 12)
backGroundColor = "#1a1a1a"
entryFont = ("Comic Sans MS", 10)
consoleColor = "black"

class CacheBlock():
	def __init__(self, root):
		self.cacheLabel = Label(root, text = "Cache", bg = backGroundColor, font = ownFont, fg = "#03b6fc")
		self.cacheLabel.grid(row = 0, column = 0, columnspan = 5)

		self.cacheP1Label = Label(root, text = "P1", bg = backGroundColor, font = ownFont, fg = "#03b6fc")
		self.cacheP1Label.grid(row = 1, column = 0)

		self.p1B0 = Text(root, width = 16, height = 3, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.p1B0.grid(row = 2, column = 0)
		self.p1B1 = Text(root, width = 16, height = 3, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.p1B1.grid(row = 3, column = 0)
		self.p1B2 = Text(root, width = 16, height = 3, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.p1B2.grid(row = 4, column = 0)
		self.p1B3 = Text(root, width = 16, height = 3, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.p1B3.grid(row = 5, column = 0)


		self.cacheP2Label = Label(root, text = "P2",bg = backGroundColor, font = ownFont, fg = "#03b6fc")
		self.cacheP2Label.grid(row = 1, column = 1)

		self.p2B0 = Text(root, width = 16, height = 3, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.p2B0.grid(row = 2, column = 1)
		self.p2B1 = Text(root, width = 16, height = 3, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.p2B1.grid(row = 3, column = 1)
		self.p2B2 = Text(root, width = 16, height = 3, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.p2B2.grid(row = 4, column = 1)
		self.p2B3 = Text(root, width = 16, height = 3, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.p2B3.grid(row = 5, column = 1)

		self.cacheP3Label = Label(root, text = "P3", bg = backGroundColor, font = ownFont, fg = "#03b6fc")
		self.cacheP3Label.grid(row = 1, column = 2)

		self.p3B0 = Text(root, width = 16, height = 3, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.p3B0.grid(row = 2, column = 2)
		self.p3B1 = Text(root, width = 16, height = 3, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.p3B1.grid(row = 3, column = 2)
		self.p3B2 = Text(root, width = 16, height = 3, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.p3B2.grid(row = 4, column = 2)
		self.p3B3 = Text(root, width = 16, height = 3, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.p3B3.grid(row = 5, column = 2)

		self.cacheP4Label = Label(root, text = "P4", bg = backGroundColor, font = ownFont, fg = "#03b6fc")
		self.cacheP4Label.grid(row = 1, column = 3)

		self.p4B0 = Text(root, width = 16, height = 3, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.p4B0.grid(row = 2, column = 3)
		self.p4B1 = Text(root, width = 16, height = 3, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.p4B1.grid(row = 3, column = 3)
		self.p4B2 = Text(root, width = 16, height = 3, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.p4B2.grid(row = 4, column = 3)
		self.p4B3 = Text(root, width = 16, height = 3, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.p4B3.grid(row = 5, column = 3)
