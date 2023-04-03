from tkinter import *
import time
# import threading

import probabilityFunction as pf



class CPU():
	def __init__(self, cpuBlock, cpuId, cacheBlock, cacheId, ram, running):
		self.cpuBlock = cpuBlock
		self.cpuId = cpuId
		self.cacheBlock = cacheBlock
		self.cacheId = cacheId
		self.ram = ram
		self.running = running

		self.lastCache0 = 0
		self.lastCache1 = 0



	def setRamValue(self, value, memAddress):
		if(memAddress == 0):
			self.ram.memAddress000.config(state = NORMAL)
			self.ram.memAddress000.delete("1.0", END)
			self.ram.memAddress000.insert(END, value)
			self.ram.memAddress000.config(state = DISABLED)

		elif(memAddress == 1):
			self.ram.memAddress001.config(state = NORMAL)
			self.ram.memAddress001.delete("1.0", END)
			self.ram.memAddress001.insert(END, value)
			self.ram.memAddress001.config(state = DISABLED)

		elif(memAddress == 2):
			self.ram.memAddress010.config(state = NORMAL)
			self.ram.memAddress010.delete("1.0", END)
			self.ram.memAddress010.insert(END, value)
			self.ram.memAddress010.config(state = DISABLED)

		elif(memAddress == 3):
			self.ram.memAddress011.config(state = NORMAL)
			self.ram.memAddress011.delete("1.0", END)
			self.ram.memAddress011.insert(END, value)
			self.ram.memAddress011.config(state = DISABLED)

		elif(memAddress == 4):
			self.ram.memAddress100.config(state = NORMAL)
			self.ram.memAddress100.delete("1.0", END)
			self.ram.memAddress100.insert(END, value)
			self.ram.memAddress100.config(state = DISABLED)
			
		elif(memAddress == 5):
			self.ram.memAddress101.config(state = NORMAL)
			self.ram.memAddress101.delete("1.0", END)
			self.ram.memAddress101.insert(END, value)
			self.ram.memAddress101.config(state = DISABLED)
			
		elif(memAddress == 6):
			self.ram.memAddress110.config(state = NORMAL)
			self.ram.memAddress110.delete("1.0", END)
			self.ram.memAddress110.insert(END, value)
			self.ram.memAddress110.config(state = DISABLED)
			
		elif(memAddress == 7):
			self.ram.memAddress111.config(state = NORMAL)
			self.ram.memAddress111.delete("1.0", END)
			self.ram.memAddress111.insert(END, value)
			self.ram.memAddress111.config(state = DISABLED)
			


	def randomInstruction(self): # CALC - READ - WRITE
		# while(True):
		instructionString = ""
		instructionType = pf.lsfr(4)
		if(instructionType == 0): # WRITE
			addressValue = self.randomAddress()
			hexValue = self.randomValue()
			instructionString = "WRITE " + (bin(addressValue)[2::]).zfill(3) + " " + hexValue
			self.setRamValue(hexValue, addressValue)

		elif(instructionType == 1): # READ
			memAddress = self.randomAddress()
			instructionString = "READ " + (bin(memAddress)[2::]).zfill(3)

		else: # CALC
			instructionString = "CALC"

		# threading.Tread(target = self.cpuBlock.updateInstructionBlock(self.cpuId, instructionString)).start()
		self.cpuBlock.updateInstructionBlock(self.cpuId, instructionString)



	def randomAddress(self): #0 - 7
		addressValue = pf.lsfr(8)
		return addressValue


	def randomValue(self): #0 - 65535
		value = pf.lsfr(65536)
		return hex(value)[2::].zfill(4)
