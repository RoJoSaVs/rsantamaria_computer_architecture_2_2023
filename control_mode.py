from tkinter import *

class ControlMode():
	def __init__(self, root):
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
		self.controlLabel = Label(root, text = "Control")
		self.controlLabel.grid(row = 0, column = 1)

		self.executionModeLabel = Label(root, text = "Execution Mode")
		self.executionModeLabel.grid(row = 1, column = 0)

		self.continueRadiobutton = Radiobutton(root, text = "Continue", variable = self.ctrlModeVal, value = 1, command = self.selection)
		self.continueRadiobutton.grid(row = 2, column = 0, sticky = W)

		self.stepByStepRadiobutton = Radiobutton(root, text = "Step by Step", variable = self.ctrlModeVal, value = 2, command = self.selection)
		self.stepByStepRadiobutton.grid(row = 3, column = 0, sticky = W)
		self.nextStepButton = Button(root, text = "Next Step", command = self.nextStep, state = "disable")
		self.nextStepButton.grid(row = 3 , column = 3)

		# User input instruction
		self.userInstructionRadiobutton = Radiobutton(root, text = "User Instruction", variable = self.ctrlModeVal, value = 3, command = self.selection)
		self.userInstructionRadiobutton.grid(row = 4, column = 0, sticky = W)

		self.cpuNumberButton = OptionMenu(root, self.cpuNumber, *self.processorNumber)
		self.cpuNumberButton.config(state = "disable")
		self.cpuNumberButton.grid(row = 4, column = 3)

		self.instructionMenuButton = OptionMenu(root, self.instructionType, *self.instructionMenu)
		self.instructionMenuButton.config(state = "disable")
		self.instructionMenuButton.grid(row = 4, column = 4)

		self.memAddressEntry = Entry(root, state = "disable")
		self.memAddressEntry.grid(row = 4, column = 5, columnspan = 1)

		self.constValEntry = Entry(root, state = "disable")
		self.constValEntry.grid(row = 4, column = 6, columnspan = 1)

		self.sendInstructionButton = Button(root, text = "Send", command = self.sendInstruction, state = "disable")
		self.sendInstructionButton.grid(row = 4 , column = 7)

		

	def selection(self):
		if(int(self.ctrlModeVal.get()) == 2):
			self.setEnable()
			self.nextStepButton["state"] = "active"

		elif(int(self.ctrlModeVal.get()) == 3):
			self.setEnable()
			self.cpuNumberButton["state"] = "active"
			self.instructionMenuButton["state"] = "active"
			self.memAddressEntry["state"] = "normal"
			self.constValEntry["state"] = "normal"
			self.sendInstructionButton["state"] = "active"

		else:
			self.setEnable()


	def setEnable(self):
		self.nextStepButton["state"] = "disable"
		self.cpuNumberButton["state"] = "disable"
		self.instructionMenuButton["state"] = "disable"
		self.sendInstructionButton["state"] = "disable"
		self.memAddressEntry["state"] = "disable"
		self.constValEntry["state"] = "disable"



	def nextStep(self):
		print("Next Step")


	def sendInstruction(self):
		print(self.cpuNumber.get() + self.instructionType.get() + self.memAddressEntry.get() + self.constValEntry.get())
