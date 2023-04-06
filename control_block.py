from tkinter import *
from tkinter import messagebox

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
		self.continueRadiobutton = Radiobutton(root, text = "Continue", variable = self.ctrlModeVal, value = 1, command = self.selection, bg = backGroundColor, font = ownFont, fg = "#03b6fc")
		self.continueRadiobutton.grid(row = 2, column = 0, sticky = W)

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
			self.running = False
			self.setDisable()
			self.nextStepButton["state"] = "active"

		elif(int(self.ctrlModeVal.get()) == 3):
			self.running = False
			self.setDisable()
			self.cpuNumberButton["state"] = "active"
			self.instructionMenuButton["state"] = "active"
			self.memAddressEntry["state"] = "normal"
			self.constValEntry["state"] = "normal"
			self.sendInstructionButton["state"] = "active"

		else:
			self.setDisable()
			self.running = True
			continuous = threading.Thread(target = self.continuousExecution).start()
			# continuous.join()


	def setDisable(self):
		self.nextStepButton["state"] = "disable"
		self.cpuNumberButton["state"] = "disable"
		self.instructionMenuButton["state"] = "disable"
		self.sendInstructionButton["state"] = "disable"
		self.memAddressEntry["state"] = "disable"
		self.constValEntry["state"] = "disable"


	def continuousExecution(self):
		while True:
			p0 = threading.Thread(target = self.cpu0.randomInstruction)
			p1 = threading.Thread(target = self.cpu1.randomInstruction)
			p2 = threading.Thread(target = self.cpu2.randomInstruction)
			p3 = threading.Thread(target = self.cpu3.randomInstruction)

			p0.start()
			p1.start()
			p2.start()
			p3.start()

			if(not(self.running)):
				break


			p0.join()
			p1.join()
			p2.join()
			p3.join()
			time.sleep(3)



	def nextStep(self):
		threading.Thread(target = self.cpu0.randomInstruction()).start()
		threading.Thread(target = self.cpu1.randomInstruction()).start()
		threading.Thread(target = self.cpu2.randomInstruction()).start()
		threading.Thread(target = self.cpu3.randomInstruction()).start()


	def sendInstruction(self):
		cpu = self.cpuNumber.get() 
		instruction = self.instructionType.get()
		address = self.memAddressEntry.get()
		value = self.constValEntry.get()
		
		if(instruction == "CALC"):
			if(self.cpuNumber.get() == "P1"):
				self.cpu0.cpuBlock.updateInstructionBlock(self.cpu0.cpuId, instruction)
				self.cpu1.randomInstruction()
				self.cpu2.randomInstruction()
				self.cpu3.randomInstruction()

			elif(self.cpuNumber.get() == "P2"):
				self.cpu1.cpuBlock.updateInstructionBlock(self.cpu1.cpuId, instruction)
				self.cpu0.randomInstruction()
				self.cpu2.randomInstruction()
				self.cpu3.randomInstruction()

			elif(self.cpuNumber.get() == "P3"):
				self.cpu2.cpuBlock.updateInstructionBlock(self.cpu2.cpuId, instruction)
				self.cpu0.randomInstruction()
				self.cpu1.randomInstruction()
				self.cpu3.randomInstruction()


			else:
				self.cpu3.cpuBlock.updateInstructionBlock(self.cpu3.cpuId, instruction)
				self.cpu0.randomInstruction()
				self.cpu1.randomInstruction()
				self.cpu2.randomInstruction()
		else:
			try:
				if(len(address) <= 3 ):
					address = int(address, 2)
					instructionString = instruction + " " + (bin(address)[2::]).zfill(3)
					if((instruction == "WRITE") and (len(value) <= 4)):
						value = int(value, 16)
						value = hex(value)[2::].zfill(4)
						instructionString = instructionString + " " + value
					else:
						value = 0
						value = hex(value)[2::].zfill(4)
					
					if(self.cpuNumber.get() == "P1"):
						self.cpu0.MOESI(instruction, address, value)
						self.cpu0.cpuBlock.updateInstructionBlock(self.cpu0.cpuId, instructionString)

						self.cpu1.randomInstruction()
						self.cpu2.randomInstruction()
						self.cpu3.randomInstruction()
					
					elif(self.cpuNumber.get() == "P2"):
						self.cpu1.MOESI(instruction, address, value)
						self.cpu1.cpuBlock.updateInstructionBlock(self.cpu1.cpuId, instructionString)

						self.cpu0.randomInstruction()
						self.cpu2.randomInstruction()
						self.cpu3.randomInstruction()

					elif(self.cpuNumber.get() == "P3"):
						self.cpu2.MOESI(instruction, address, value)
						self.cpu2.cpuBlock.updateInstructionBlock(self.cpu2.cpuId, instructionString)

						self.cpu0.randomInstruction()
						self.cpu1.randomInstruction()
						self.cpu3.randomInstruction()
					
					else:
						self.cpu3.MOESI(instruction, address, value)
						self.cpu3.cpuBlock.updateInstructionBlock(self.cpu3.cpuId, instructionString)

						self.cpu0.randomInstruction()
						self.cpu1.randomInstruction()
						self.cpu2.randomInstruction()

			except:
				messagebox.showerror("Wrong value input", "Invalid values for input: \n - Address: (000 - 111) \n - Value: (0000 - ffff)")

			
