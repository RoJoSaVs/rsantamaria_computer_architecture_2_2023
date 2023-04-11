from tkinter import *



class Cache():
	def __init__(self, cacheStatus, cacheValue, cacheAddress):
		self.cacheStatus = cacheStatus
		self.cacheValue = cacheValue
		self.cacheAddress = cacheAddress


	def setValue(self, value):
		self.cacheValue = value

	def setStatus(self, status):
		self.cacheStatus = status

	def setAddress(self, address):
		self.cacheAddress = address


	def getValue(self):
		return self.cacheValue

	def getStatus(self):
		return self.cacheStatus

	def getAddress(self):
		return self.cacheAddress
