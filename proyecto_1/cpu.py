from tkinter import *
import time
import random

import probabilityFunction as pf
from cache_control import *
from constants import *



class CPU():
	def __init__(self, cpuBlock, cpuId, cacheBlock, cacheId, ram, running):
		self.cpuBlock = cpuBlock
		self.cpuId = cpuId
		self.cacheBlock = cacheBlock
		self.cacheId = cacheId
		self.ram = ram
		self.running = running

		self.lastCache = [1, 1]


	def MOESI(self, instruction, memAddress, value):
		listCachesWithAddress = self.getCacheWithAddress(memAddress)

		if(instruction == "READ"):
			if(listCachesWithAddress == []):
				self.updateCacheStatus(memAddress, "E", ramModelVector[memAddress])
				self.cacheBlock.updateCacheGui()

			else:
				for cache in listCachesWithAddress:
					# https://developer.arm.com/documentation/den0013/d/Multi-core-processors/Cache-coherency/MESI-and-MOESI-protocols
					if(cache.getStatus() == "M"): # Cache => O  Cache' => S
						# ramModelVector[int('0b' + cache.getAddress(), 2)] = cache.getValue() # Write to RAM
						# self.ram.updateRamValue()
						cache.setStatus("O")
						self.updateCacheStatus(memAddress, "S", cache.getValue())


					elif(cache.getStatus() == "O"):
						self.updateCacheStatus(memAddress, "S", cache.getValue())

					elif(cache.getStatus() == "E"):
						cache.setStatus("S")
						self.updateCacheStatus(memAddress, "S", cache.getValue())


					elif(cache.getStatus() == "S"):
						cache.setStatus("S")
						self.updateCacheStatus(memAddress, "S", cache.getValue())

					elif(cache.getStatus() == "I"):
						self.updateCacheStatus(memAddress, "E", ramModelVector[memAddress]) # Read from RAM

		elif(instruction == "WRITE"):
			writeOnCache = False
			for cache in listCachesWithAddress:
				if(cache.getStatus() == "O"):
					writeOnCache = True

			if(writeOnCache):
				pass

			else:
				self.updateCacheStatus(memAddress, "M", value)
				for cache in listCachesWithAddress:
					cache.setStatus("I")

			self.cacheBlock.updateCacheGui()






	def updateCacheStatus(self, address, status, value): # BUS
		existingCache = self.getCacheWithAddressLocalCPU(address)
		if (address % 2 == 0):
			if(existingCache == None):
				pass
			else:
				if(self.lastCache[0] == 1):
					self.lastCache[0] = 0
				else:
					self.lastCache[0] = 1

			if(self.lastCache[0] == 1): # Modify set 0 0
				if((cacheModelMatrix[self.cpuId][0].getStatus() == "M") or (cacheModelMatrix[self.cpuId][0].getStatus() == "O")):
					ramModelVector[address] = cacheModelMatrix[self.cpuId][0].getValue() # Write to RAM
					self.ram.updateRamValue()
				cacheModelMatrix[self.cpuId][0].setValue(value)
				cacheModelMatrix[self.cpuId][0].setStatus(status)
				cacheModelMatrix[self.cpuId][0].setAddress((bin(address)[2::]).zfill(3))
				self.cacheBlock.updateCacheGui()
				self.lastCache[0] = 0

			else: # Modify set 0 1
				if((cacheModelMatrix[self.cpuId][1].getStatus() == "M") or (cacheModelMatrix[self.cpuId][1].getStatus() == "O")):
					ramModelVector[address] = cacheModelMatrix[self.cpuId][1].getValue() # Write to RAM
					self.ram.updateRamValue()
				cacheModelMatrix[self.cpuId][1].setValue(value)
				cacheModelMatrix[self.cpuId][1].setStatus(status)
				cacheModelMatrix[self.cpuId][1].setAddress((bin(address)[2::]).zfill(3))
				self.cacheBlock.updateCacheGui()
				self.lastCache[0] = 1

		else:
			if(existingCache == None):
				pass
			else:
				if(self.lastCache[1] == 1):
					self.lastCache[1] = 0
				else:
					self.lastCache[1] = 1

			if(self.lastCache[1] == 1): # Modify set 1 0
				if((cacheModelMatrix[self.cpuId][2].getStatus() == "M") or (cacheModelMatrix[self.cpuId][2].getStatus() == "O")):
					ramModelVector[address] = cacheModelMatrix[self.cpuId][2].getValue() # Write to RAM
					self.ram.updateRamValue()
				cacheModelMatrix[self.cpuId][2].setValue(value)
				cacheModelMatrix[self.cpuId][2].setStatus(status)
				cacheModelMatrix[self.cpuId][2].setAddress((bin(address)[2::]).zfill(3))
				self.cacheBlock.updateCacheGui()
				self.lastCache[1] = 0

			else: # Modify set 1 1
				if((cacheModelMatrix[self.cpuId][3].getStatus() == "M") or (cacheModelMatrix[self.cpuId][3].getStatus() == "O")):
					ramModelVector[address] = cacheModelMatrix[self.cpuId][3].getValue() # Write to RAM
					self.ram.updateRamValue()
				cacheModelMatrix[self.cpuId][3].setValue(value)
				cacheModelMatrix[self.cpuId][3].setStatus(status)
				cacheModelMatrix[self.cpuId][3].setAddress((bin(address)[2::]).zfill(3))
				self.cacheBlock.updateCacheGui()
				self.lastCache[1] = 1


	def getCacheWithAddress(self, memAddress):
		listOfCache = []
		for row in range(0, len(cacheModelMatrix)):
			if(row != self.cpuId):
				for column in range(0, len(cacheModelMatrix[row])):
					if(cacheModelMatrix[row][column].getAddress() == (bin(memAddress)[2::]).zfill(3)):
						listOfCache.append(cacheModelMatrix[row][column])
		return listOfCache

	def getCacheWithAddressLocalCPU(self, memAddress):
		for cache in cacheModelMatrix[self.cpuId]:
			if(cache.getAddress() == (bin(memAddress)[2::]).zfill(3)):
				return cache
		return None


	def randomInstruction(self): # CALC - READ - WRITE
		instructionString = ""
		instructionType = pf.randomNumber(100)

		# Discrete Uniform Distribution
		if(instructionType < 33): # WRITE
			memAddress = self.randomAddress()
			hexValue = self.randomValue()
			instructionString = "WRITE " + (bin(memAddress)[2::]).zfill(3) + " " + hexValue
			self.MOESI("WRITE", memAddress, hexValue)


		elif(instructionType < 66): # READ
			memAddress = self.randomAddress()
			instructionString = "READ " + (bin(memAddress)[2::]).zfill(3)
			self.MOESI("READ", memAddress, "0000")

		else: # CALC
			instructionString = "CALC"

		self.cpuBlock.updateInstructionBlock(self.cpuId, instructionString)


	def randomAddress(self): #0 - 7
		addressValue = pf.randomNumber(80) # Discrete Uniform Distribution with mod
		return addressValue % 8


	def randomValue(self): #0 - 65535
		value = int(random.uniform(0, 65535))
		return hex(value)[2::].zfill(4)
