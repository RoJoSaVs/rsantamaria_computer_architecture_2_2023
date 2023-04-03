from tkinter import *
import threading
import time


ownFont = ("Comic Sans MS", 12)
bottonFont = ("Comic Sans MS", 10)
backGroundColor = "#1a1a1a"
consoleColor = "black"

class ControlBlock():
	def __init__(self, root, cpu0, cpu1, cpu2, cpu3):
		self.cpu0 = cpu0
		self.cpu1 = cpu1
		self.cpu2 = cpu2
		self.cpu3 = cpu3
		self.running = True
		# self.running = threading.Event()

		# Control Variables
		self.ctrlModeVal = IntVar()
		self.instructionType = StringVar()
		self.cpuNumber = StringVar()
		self.memoryAddress = StringVar()
		self.constantValue = StringVar()


		self.processorNumber = ["P1", "P2", "P3", "P4"]
		self.cpuNumber.set(self.processorNumber[0])

		self.instructionMenu = ["CALC", "WRITE", "READ"]
		self.instructionType.set(self.instructionMenu[0])


		# GUI stuff
		self.controlLabel = Label(root, text = "Control", bg = backGroundColor, font = ownFont, fg = "#03b6fc")
		self.controlLabel.grid(row = 0, column = 1)

		self.executionModeLabel = Label(root, text = "Execution Mode", bg = backGroundColor, font = ownFont, fg = "#03b6fc")
		self.executionModeLabel.grid(row = 1, column = 0)

		# Continue Exec needs thread implementation
		# self.continueRadiobutton = Radiobutton(root, text = "Continue", variable = self.ctrlModeVal, value = 1, command = self.selection, bg = backGroundColor, font = ownFont, fg = "#03b6fc")
		# self.continueRadiobutton.grid(row = 2, column = 0, sticky = W)

		self.stepByStepRadiobutton = Radiobutton(root, text = "Step by Step", variable = self.ctrlModeVal, value = 2, command = self.selection, bg = backGroundColor, font = ownFont, fg = "#03b6fc")
		self.stepByStepRadiobutton.grid(row = 3, column = 0, sticky = W)
		self.nextStepButton = Button(root, text = "Next Step", command = self.nextStep, state = "disable", bg = backGroundColor, font = bottonFont, fg = "#03b6fc")
		self.nextStepButton.grid(row = 3 , column = 1)

		# User input instruction
		self.userInstructionRadiobutton = Radiobutton(root, text = "User Instruction", variable = self.ctrlModeVal, value = 3, command = self.selection, bg = backGroundColor, font = ownFont, fg = "#03b6fc")
		self.userInstructionRadiobutton.grid(row = 4, column = 0, sticky = W)

		self.cpuNumberButton = OptionMenu(root, self.cpuNumber, *self.processorNumber)
		self.cpuNumberButton.config(state = "disable", bg = backGroundColor, font = bottonFont, fg = "#03b6fc")
		self.cpuNumberButton.grid(row = 4, column = 1)

		self.instructionMenuButton = OptionMenu(root, self.instructionType, *self.instructionMenu)
		self.instructionMenuButton.config(state = "disable", bg = backGroundColor, font = bottonFont, fg = "#03b6fc")
		self.instructionMenuButton.grid(row = 4, column = 3)

		self.memAddressEntry = Entry(root, state = "disable", bg = consoleColor, font = bottonFont, fg = "#05fa42")
		self.memAddressEntry.grid(row = 4, column = 4)

		self.constValEntry = Entry(root, state = "disable", bg = consoleColor, font = bottonFont, fg = "#05fa42")
		self.constValEntry.grid(row = 4, column = 5)

		self.sendInstructionButton = Button(root, text = "Send", command = self.sendInstruction, state = "disable", bg = backGroundColor, font = bottonFont, fg = "#03b6fc")
		self.sendInstructionButton.grid(row = 4 , column = 6)

		

	def selection(self):
		if(int(self.ctrlModeVal.get()) == 2):
			self.setDisable()
			self.nextStepButton["state"] = "active"

		elif(int(self.ctrlModeVal.get()) == 3):
			# self.continueExec = False

			self.setDisable()
			self.cpuNumberButton["state"] = "active"
			self.instructionMenuButton["state"] = "active"
			self.memAddressEntry["state"] = "normal"
			self.constValEntry["state"] = "normal"
			self.sendInstructionButton["state"] = "active"

		else:
			self.setDisable()
			threading.Thread(target = self.continuousExecution(True)).start()


	def setDisable(self):
		# self.running = False
		self.nextStepButton["state"] = "disable"
		self.cpuNumberButton["state"] = "disable"
		self.instructionMenuButton["state"] = "disable"
		self.sendInstructionButton["state"] = "disable"
		self.memAddressEntry["state"] = "disable"
		self.constValEntry["state"] = "disable"


	def continuousExecution(self, running):
		# print(self.running)
		while self.running:
			if(running):
				threading.Thread(target = self.cpu0.randomInstruction()).start()
				threading.Thread(target = self.cpu1.randomInstruction()).start()
				threading.Thread(target = self.cpu2.randomInstruction()).start()
				threading.Thread(target = self.cpu3.randomInstruction()).start()
				running = False
			else:
				running = True
			# print("2")
			# self.cpu0.randomInstruction()
			# self.cpu1.randomInstruction()
			# self.cpu2.randomInstruction()
			# self.cpu3.randomInstruction()
			time.sleep(1)
			# threading.Thread(target = self.cpu0.randomInstruction(), args=(1,)).start()



	def nextStep(self):
		threading.Thread(target = self.cpu0.randomInstruction()).start()
		threading.Thread(target = self.cpu1.randomInstruction()).start()
		threading.Thread(target = self.cpu2.randomInstruction()).start()
		threading.Thread(target = self.cpu3.randomInstruction()).start()
		# print("Next Step")


	def sendInstruction(self):
		print(self.cpuNumber.get() + self.instructionType.get() + self.memAddressEntry.get() + self.constValEntry.get())
