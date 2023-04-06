from tkinter import *
from constants import *
from cache_control import *

ownFont = ("Comic Sans MS", 12)
backGroundColor = "#1a1a1a"
entryFont = ("Comic Sans MS", 10)
consoleColor = "black"

class CacheBlock():
	def __init__(self, root):
		self.cacheLabel = Label(root, text = "Cache", bg = backGroundColor, font = ownFont, fg = "#03b6fc")
		self.cacheLabel.grid(row = 0, column = 0, columnspan = 5)

		self.cacheP0Label = Label(root, text = "P1", bg = backGroundColor, font = ownFont, fg = "#03b6fc")
		self.cacheP0Label.grid(row = 1, column = 0)

		self.p0B0 = Text(root, width = 16, height = 3, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.p0B0.grid(row = 2, column = 0)
		self.p0B1 = Text(root, width = 16, height = 3, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.p0B1.grid(row = 3, column = 0)
		self.p0B2 = Text(root, width = 16, height = 3, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.p0B2.grid(row = 4, column = 0)
		self.p0B3 = Text(root, width = 16, height = 3, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.p0B3.grid(row = 5, column = 0)


		self.cacheP1Label = Label(root, text = "P2",bg = backGroundColor, font = ownFont, fg = "#03b6fc")
		self.cacheP1Label.grid(row = 1, column = 1)

		self.p1B0 = Text(root, width = 16, height = 3, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.p1B0.grid(row = 2, column = 1)
		self.p1B1 = Text(root, width = 16, height = 3, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.p1B1.grid(row = 3, column = 1)
		self.p1B2 = Text(root, width = 16, height = 3, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.p1B2.grid(row = 4, column = 1)
		self.p1B3 = Text(root, width = 16, height = 3, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.p1B3.grid(row = 5, column = 1)

		self.cacheP2Label = Label(root, text = "P3", bg = backGroundColor, font = ownFont, fg = "#03b6fc")
		self.cacheP2Label.grid(row = 1, column = 2)

		self.p2B0 = Text(root, width = 16, height = 3, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.p2B0.grid(row = 2, column = 2)
		self.p2B1 = Text(root, width = 16, height = 3, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.p2B1.grid(row = 3, column = 2)
		self.p2B2 = Text(root, width = 16, height = 3, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.p2B2.grid(row = 4, column = 2)
		self.p2B3 = Text(root, width = 16, height = 3, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.p2B3.grid(row = 5, column = 2)

		self.cacheP3Label = Label(root, text = "P4", bg = backGroundColor, font = ownFont, fg = "#03b6fc")
		self.cacheP3Label.grid(row = 1, column = 3)

		self.p3B0 = Text(root, width = 16, height = 3, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.p3B0.grid(row = 2, column = 3)
		self.p3B1 = Text(root, width = 16, height = 3, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.p3B1.grid(row = 3, column = 3)
		self.p3B2 = Text(root, width = 16, height = 3, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.p3B2.grid(row = 4, column = 3)
		self.p3B3 = Text(root, width = 16, height = 3, state = "disable", bg = consoleColor, font = entryFont, fg = "#05fa42")
		self.p3B3.grid(row = 5, column = 3)

	def startCache(self):
		self.p0B0.config(state = NORMAL)
		self.p0B0.insert(END, "status: I\naddress: xxx\ndata: 0000")
		self.p0B0.config(state = DISABLED)
		self.p0B1.config(state = NORMAL)
		self.p0B1.insert(END, "status: I\naddress: xxx\ndata: 0000")
		self.p0B1.config(state = DISABLED)
		self.p0B2.config(state = NORMAL)
		self.p0B2.insert(END, "status: I\naddress: xxx\ndata: 0000")
		self.p0B2.config(state = DISABLED)
		self.p0B3.config(state = NORMAL)
		self.p0B3.insert(END, "status: I\naddress: xxx\ndata: 0000")
		self.p0B3.config(state = DISABLED)

		self.p1B0.config(state = NORMAL)
		self.p1B0.insert(END, "status: I\naddress: xxx\ndata: 0000")
		self.p1B0.config(state = DISABLED)
		self.p1B1.config(state = NORMAL)
		self.p1B1.insert(END, "status: I\naddress: xxx\ndata: 0000")
		self.p1B1.config(state = DISABLED)
		self.p1B2.config(state = NORMAL)
		self.p1B2.insert(END, "status: I\naddress: xxx\ndata: 0000")
		self.p1B2.config(state = DISABLED)
		self.p1B3.config(state = NORMAL)
		self.p1B3.insert(END, "status: I\naddress: xxx\ndata: 0000")
		self.p1B3.config(state = DISABLED)

		self.p2B0.config(state = NORMAL)
		self.p2B0.insert(END, "status: I\naddress: xxx\ndata: 0000")
		self.p2B0.config(state = DISABLED)
		self.p2B1.config(state = NORMAL)
		self.p2B1.insert(END, "status: I\naddress: xxx\ndata: 0000")
		self.p2B1.config(state = DISABLED)
		self.p2B2.config(state = NORMAL)
		self.p2B2.insert(END, "status: I\naddress: xxx\ndata: 0000")
		self.p2B2.config(state = DISABLED)
		self.p2B3.config(state = NORMAL)
		self.p2B3.insert(END, "status: I\naddress: xxx\ndata: 0000")
		self.p2B3.config(state = DISABLED)

		self.p3B0.config(state = NORMAL)
		self.p3B0.insert(END, "status: I\naddress: xxx\ndata: 0000")
		self.p3B0.config(state = DISABLED)
		self.p3B1.config(state = NORMAL)
		self.p3B1.insert(END, "status: I\naddress: xxx\ndata: 0000")
		self.p3B1.config(state = DISABLED)
		self.p3B2.config(state = NORMAL)
		self.p3B2.insert(END, "status: I\naddress: xxx\ndata: 0000")
		self.p3B2.config(state = DISABLED)
		self.p3B3.config(state = NORMAL)
		self.p3B3.insert(END, "status: I\naddress: xxx\ndata: 0000")
		self.p3B3.config(state = DISABLED)


	def updateCacheGui(self):
		self.p0B0.config(state = NORMAL, foreground = "#05fa42")
		self.p0B0.delete("1.0", END)
		self.p0B0.insert(END, "status: " + cacheModelMatrix[0][0].getStatus() +"\naddress: " + cacheModelMatrix[0][0].getAddress() + "\ndata: " + cacheModelMatrix[0][0].getValue())
		if(cacheModelMatrix[0][0].getStatus() == "E"):
			self.p0B0.config(foreground = "red")
		self.p0B0.config(state = DISABLED)

		self.p0B1.config(state = NORMAL, foreground = "#05fa42")
		self.p0B1.delete("1.0", END)
		self.p0B1.insert(END, "status: " + cacheModelMatrix[0][1].getStatus() +"\naddress: " + cacheModelMatrix[0][1].getAddress() + "\ndata: " + cacheModelMatrix[0][1].getValue())
		if(cacheModelMatrix[0][1].getStatus() == "E"):
			self.p0B1.config(foreground = "red")
		self.p0B1.config(state = DISABLED)
		
		self.p0B2.config(state = NORMAL, foreground = "#05fa42")
		self.p0B2.delete("1.0", END)
		self.p0B2.insert(END, "status: " + cacheModelMatrix[0][2].getStatus() +"\naddress: " + cacheModelMatrix[0][2].getAddress() + "\ndata: " + cacheModelMatrix[0][2].getValue())
		if(cacheModelMatrix[0][2].getStatus() == "E"):
			self.p0B2.config(foreground = "red")
		self.p0B2.config(state = DISABLED)

		self.p0B3.config(state = NORMAL, foreground = "#05fa42")
		self.p0B3.delete("1.0", END)
		self.p0B3.insert(END, "status: " + cacheModelMatrix[0][3].getStatus() +"\naddress: " + cacheModelMatrix[0][3].getAddress() + "\ndata: " + cacheModelMatrix[0][3].getValue())
		if(cacheModelMatrix[0][3].getStatus() == "E"):
			self.p0B3.config(foreground = "red")
		self.p0B3.config(state = DISABLED)

		self.p1B0.config(state = NORMAL, foreground = "#05fa42")
		self.p1B0.delete("1.0", END)
		self.p1B0.insert(END, "status: " + cacheModelMatrix[1][0].getStatus() +"\naddress: " + cacheModelMatrix[1][0].getAddress() + "\ndata: " + cacheModelMatrix[1][0].getValue())
		if(cacheModelMatrix[1][0].getStatus() == "E"):
			self.p1B0.config(foreground = "red")
		self.p1B0.config(state = DISABLED)

		self.p1B1.config(state = NORMAL, foreground = "#05fa42")
		self.p1B1.delete("1.0", END)
		self.p1B1.insert(END, "status: " + cacheModelMatrix[1][1].getStatus() +"\naddress: " + cacheModelMatrix[1][1].getAddress() + "\ndata: " + cacheModelMatrix[1][1].getValue())
		if(cacheModelMatrix[1][1].getStatus() == "E"):
			self.p1B1.config(foreground = "red")
		self.p1B1.config(state = DISABLED)

		self.p1B2.config(state = NORMAL, foreground = "#05fa42")
		self.p1B2.delete("1.0", END)
		self.p1B2.insert(END, "status: " + cacheModelMatrix[1][2].getStatus() +"\naddress: " + cacheModelMatrix[1][2].getAddress() + "\ndata: " + cacheModelMatrix[1][2].getValue())
		if(cacheModelMatrix[1][2].getStatus() == "E"):
			self.p1B2.config(foreground = "red")
		self.p1B2.config(state = DISABLED)

		self.p1B3.config(state = NORMAL, foreground = "#05fa42")
		self.p1B3.delete("1.0", END)
		self.p1B3.insert(END, "status: " + cacheModelMatrix[1][3].getStatus() +"\naddress: " + cacheModelMatrix[1][3].getAddress() + "\ndata: " + cacheModelMatrix[1][3].getValue())
		if(cacheModelMatrix[1][3].getStatus() == "E"):
			self.p1B3.config(foreground = "red")
		self.p1B3.config(state = DISABLED)

		self.p2B0.config(state = NORMAL, foreground = "#05fa42")
		self.p2B0.delete("1.0", END)
		self.p2B0.insert(END, "status: " + cacheModelMatrix[2][0].getStatus() +"\naddress: " + cacheModelMatrix[2][0].getAddress() + "\ndata: " + cacheModelMatrix[2][0].getValue())
		if(cacheModelMatrix[2][0].getStatus() == "E"):
			self.p2B0.config(foreground = "red")
		self.p2B0.config(state = DISABLED)

		self.p2B1.config(state = NORMAL, foreground = "#05fa42")
		self.p2B1.delete("1.0", END)
		self.p2B1.insert(END, "status: " + cacheModelMatrix[2][1].getStatus() +"\naddress: " + cacheModelMatrix[2][1].getAddress() + "\ndata: " + cacheModelMatrix[2][1].getValue())
		if(cacheModelMatrix[2][1].getStatus() == "E"):
			self.p2B1.config(foreground = "red")
		self.p2B1.config(state = DISABLED)

		self.p2B2.config(state = NORMAL, foreground = "#05fa42")
		self.p2B2.delete("1.0", END)
		self.p2B2.insert(END, "status: " + cacheModelMatrix[2][2].getStatus() +"\naddress: " + cacheModelMatrix[2][2].getAddress() + "\ndata: " + cacheModelMatrix[2][2].getValue())
		if(cacheModelMatrix[2][2].getStatus() == "E"):
			self.p2B2.config(foreground = "red")
		self.p2B2.config(state = DISABLED)

		self.p2B3.config(state = NORMAL, foreground = "#05fa42")
		self.p2B3.delete("1.0", END)
		self.p2B3.insert(END, "status: " + cacheModelMatrix[2][3].getStatus() +"\naddress: " + cacheModelMatrix[2][3].getAddress() + "\ndata: " + cacheModelMatrix[2][3].getValue())
		if(cacheModelMatrix[2][3].getStatus() == "E"):
			self.p2B3.config(foreground = "red")
		self.p2B3.config(state = DISABLED)

		self.p3B0.config(state = NORMAL, foreground = "#05fa42")
		self.p3B0.delete("1.0", END)
		self.p3B0.insert(END, "status: " + cacheModelMatrix[3][0].getStatus() +"\naddress: " + cacheModelMatrix[3][0].getAddress() + "\ndata: " + cacheModelMatrix[3][0].getValue())
		if(cacheModelMatrix[3][0].getStatus() == "E"):
			self.p3B0.config(foreground = "red")
		self.p3B0.config(state = DISABLED)

		self.p3B1.config(state = NORMAL, foreground = "#05fa42")
		self.p3B1.delete("1.0", END)
		self.p3B1.insert(END, "status: " + cacheModelMatrix[3][1].getStatus() +"\naddress: " + cacheModelMatrix[3][1].getAddress() + "\ndata: " + cacheModelMatrix[3][1].getValue())
		if(cacheModelMatrix[3][1].getStatus() == "E"):
			self.p3B1.config(foreground = "red")
		self.p3B1.config(state = DISABLED)

		self.p3B2.config(state = NORMAL, foreground = "#05fa42")
		self.p3B2.delete("1.0", END)
		self.p3B2.insert(END, "status: " + cacheModelMatrix[3][2].getStatus() +"\naddress: " + cacheModelMatrix[3][2].getAddress() + "\ndata: " + cacheModelMatrix[3][2].getValue())
		if(cacheModelMatrix[3][2].getStatus() == "E"):
			self.p3B2.config(foreground = "red")
		self.p3B2.config(state = DISABLED)

		self.p3B3.config(state = NORMAL, foreground = "#05fa42")
		self.p3B3.delete("1.0", END)
		self.p3B3.insert(END, "status: " + cacheModelMatrix[3][3].getStatus() +"\naddress: " + cacheModelMatrix[3][3].getAddress() + "\ndata: " + cacheModelMatrix[3][3].getValue())
		if(cacheModelMatrix[3][3].getStatus() == "E"):
			self.p3B3.config(foreground = "red")
		self.p3B3.config(state = DISABLED)


	def missAlert(self, cacheId):
		if(cacheId == 0):
			self.p0B0.config(foreground = "red")
			# self.p0B0.delete("1.0", END)
			# self.p0B0.insert(END, "status: " + cacheModelMatrix[0][0].getStatus() +"\naddress: " + cacheModelMatrix[0][0].getAddress() + "\ndata: " + cacheModelMatrix[0][0].getValue())
			# self.p0B0.config(state = DISABLED)

		elif(cacheId == 1):
			self.p0B1.config(foreground = "red")
			# self.p0B1.delete("1.0", END)
			# self.p0B1.insert(END, "status: " + cacheModelMatrix[0][1].getStatus() +"\naddress: " + cacheModelMatrix[0][1].getAddress() + "\ndata: " + cacheModelMatrix[0][1].getValue())
			# self.p0B1.config(state = DISABLED)

		elif(cacheId == 2):
			self.p0B2.config(foreground = "red")
			# self.p0B2.delete("1.0", END)
			# self.p0B2.insert(END, "status: " + cacheModelMatrix[0][2].getStatus() +"\naddress: " + cacheModelMatrix[0][2].getAddress() + "\ndata: " + cacheModelMatrix[0][2].getValue())
			# self.p0B2.config(state = DISABLED)

		elif(cacheId == 3):
			self.p0B3.config(foreground = "red")
			# self.p0B3.delete("1.0", END)
			# self.p0B3.insert(END, "status: " + cacheModelMatrix[0][3].getStatus() +"\naddress: " + cacheModelMatrix[0][3].getAddress() + "\ndata: " + cacheModelMatrix[0][3].getValue())
			# self.p0B3.config(state = DISABLED)

		elif(cacheId == 4):
			self.p1B0.config(foreground = "red")
			# self.p1B0.delete("1.0", END)
			# self.p1B0.insert(END, "status: " + cacheModelMatrix[1][0].getStatus() +"\naddress: " + cacheModelMatrix[1][0].getAddress() + "\ndata: " + cacheModelMatrix[1][0].getValue())
			# self.p1B0.config(state = DISABLED)

		elif(cacheId == 5):
			self.p1B1.config(foreground = "red")
			# self.p1B1.delete("1.0", END)
			# self.p1B1.insert(END, "status: " + cacheModelMatrix[1][1].getStatus() +"\naddress: " + cacheModelMatrix[1][1].getAddress() + "\ndata: " + cacheModelMatrix[1][1].getValue())
			# self.p1B1.config(state = DISABLED)

		elif(cacheId == 6):
			self.p1B2.config(foreground = "red")
			# self.p1B2.delete("1.0", END)
			# self.p1B2.insert(END, "status: " + cacheModelMatrix[1][2].getStatus() +"\naddress: " + cacheModelMatrix[1][2].getAddress() + "\ndata: " + cacheModelMatrix[1][2].getValue())
			# self.p1B2.config(state = DISABLED)

		elif(cacheId == 7):
			self.p1B3.config(foreground = "red")
			# self.p1B3.delete("1.0", END)
			# self.p1B3.insert(END, "status: " + cacheModelMatrix[1][3].getStatus() +"\naddress: " + cacheModelMatrix[1][3].getAddress() + "\ndata: " + cacheModelMatrix[1][3].getValue())
			# self.p1B3.config(state = DISABLED)

		elif(cacheId == 8):
			self.p2B0.config(foreground = "red")
			# self.p2B0.delete("1.0", END)
			# self.p2B0.insert(END, "status: " + cacheModelMatrix[2][0].getStatus() +"\naddress: " + cacheModelMatrix[2][0].getAddress() + "\ndata: " + cacheModelMatrix[2][0].getValue())
			# self.p2B0.config(state = DISABLED)

		elif(cacheId == 9):
			self.p2B1.config(foreground = "red")
			# self.p2B1.delete("1.0", END)
			# self.p2B1.insert(END, "status: " + cacheModelMatrix[2][1].getStatus() +"\naddress: " + cacheModelMatrix[2][1].getAddress() + "\ndata: " + cacheModelMatrix[2][1].getValue())
			# self.p2B1.config(state = DISABLED)

		elif(cacheId == 10):
			self.p2B2.config(foreground = "red")
			# self.p2B2.delete("1.0", END)
			# self.p2B2.insert(END, "status: " + cacheModelMatrix[2][2].getStatus() +"\naddress: " + cacheModelMatrix[2][2].getAddress() + "\ndata: " + cacheModelMatrix[2][2].getValue())
			# self.p2B2.config(state = DISABLED)

		elif(cacheId == 11):
			self.p2B3.config(foreground = "red")
			# self.p2B3.delete("1.0", END)
			# self.p2B3.insert(END, "status: " + cacheModelMatrix[2][3].getStatus() +"\naddress: " + cacheModelMatrix[2][3].getAddress() + "\ndata: " + cacheModelMatrix[2][3].getValue())
			# self.p2B3.config(state = DISABLED)

		elif(cacheId == 12):
			self.p3B0.config(foreground = "red")
			# self.p3B0.delete("1.0", END)
			# self.p3B0.insert(END, "status: " + cacheModelMatrix[3][0].getStatus() +"\naddress: " + cacheModelMatrix[3][0].getAddress() + "\ndata: " + cacheModelMatrix[3][0].getValue())
			# self.p3B0.config(state = DISABLED)

		elif(cacheId == 13):
			self.p3B1.config(foreground = "red")
			# self.p3B1.delete("1.0", END)
			# self.p3B1.insert(END, "status: " + cacheModelMatrix[3][1].getStatus() +"\naddress: " + cacheModelMatrix[3][1].getAddress() + "\ndata: " + cacheModelMatrix[3][1].getValue())
			# self.p3B1.config(state = DISABLED)

		elif(cacheId == 14):
			self.p3B2.config(foreground = "red")
			# self.p3B2.delete("1.0", END)
			# self.p3B2.insert(END, "status: " + cacheModelMatrix[3][2].getStatus() +"\naddress: " + cacheModelMatrix[3][2].getAddress() + "\ndata: " + cacheModelMatrix[3][2].getValue())
			# self.p3B2.config(state = DISABLED)

		elif(cacheId == 15):
			self.p3B3.config(foreground = "red")
			# self.p3B3.delete("1.0", END)
			# self.p3B3.insert(END, "status: " + cacheModelMatrix[3][3].getStatus() +"\naddress: " + cacheModelMatrix[3][3].getAddress() + "\ndata: " + cacheModelMatrix[3][3].getValue())
			# self.p3B3.config(state = DISABLED)