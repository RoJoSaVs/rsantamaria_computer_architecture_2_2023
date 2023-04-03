import time
import random

def timeNumber():
	return int(time.perf_counter())




def lsfr(modNum):
	# seed = timeNumber()
	seed = int(random.uniform(0, modNum))
	# for i in range(0, 10):
	# 	newBit = ((seed >> 1) & 1) ^ (seed & 1)
	# 	newBit = newBit * 8
	# 	seed = seed >> 1
	# 	seed = seed + newBit
	# return seed % modNum
	return seed


# print(lsfr(timeNumber(), 4))