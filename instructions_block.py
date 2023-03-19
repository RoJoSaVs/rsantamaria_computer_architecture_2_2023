from tkinter import *

class InstructionsBlock():
	def __init__(self, root):
		
		self.instructionLabel = Label(root, text = "Instructions")
		self.instructionLabel.grid(row = 0, column = 0, columnspan = 7)

		self.p1Label = Label(root, text = "P1")
		self.p1Label.grid(row = 1, column = 0)
		self.instProc1 = Text(root, width=20, height=10)
		self.instProc1.config(state=DISABLED)
		self.instProc1.grid(row=2, column=0, padx=2)

		self.p2Label = Label(root, text = "P2")
		self.p2Label.grid(row = 1, column = 1)
		self.instProc2 = Text(root, width=20, height=10)
		self.instProc2.config(state=DISABLED)
		self.instProc2.grid(row=2, column=1, padx=2)

		self.p3Label = Label(root, text = "P3")
		self.p3Label.grid(row = 1, column = 2)
		self.instProc3 = Text(root, width=20, height=10)
		self.instProc3.config(state=DISABLED)
		self.instProc3.grid(row=2, column=2, padx=2)

		self.p4Label = Label(root, text = "P4")
		self.p4Label.grid(row = 1, column = 3)
		self.instProc4 = Text(root, width=20, height=10)
		self.instProc4.config(state=DISABLED)
		self.instProc4.grid(row=2, column=3, padx=2)