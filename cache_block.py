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
		self.p1CacheCurrent = Text(root, width = 16, height = 5, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.p1CacheCurrent.grid(row = 2, column = 0)
		self.p1CachePrev = Text(root, width = 16, height = 5, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.p1CachePrev.grid(row = 3, column = 0)

		self.cacheP2Label = Label(root, text = "P2",bg = backGroundColor, font = ownFont, fg = "#03b6fc")
		self.cacheP2Label.grid(row = 1, column = 1)
		self.p2CacheCurrent = Text(root, width = 16, height = 5, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.p2CacheCurrent.grid(row = 2, column = 1)
		self.p2CachePrev = Text(root, width = 16, height = 5, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.p2CachePrev.grid(row = 3, column = 1)

		self.cacheP3Label = Label(root, text = "P3", bg = backGroundColor, font = ownFont, fg = "#03b6fc")
		self.cacheP3Label.grid(row = 1, column = 2)
		self.p3CacheCurrent = Text(root, width = 16, height = 5, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.p3CacheCurrent.grid(row = 2, column = 2)
		self.p3CachePrev = Text(root, width = 16, height = 5, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.p3CachePrev.grid(row = 3, column = 2)

		self.cacheP4Label = Label(root, text = "P4", bg = backGroundColor, font = ownFont, fg = "#03b6fc")
		self.cacheP4Label.grid(row = 1, column = 3)
		self.p4CacheCurrent = Text(root, width = 16, height = 5, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.p4CacheCurrent.grid(row = 2, column = 3)
		self.p4CachePrev = Text(root, width = 16, height = 5, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.p4CachePrev.grid(row = 3, column = 3)
