import threading

from control_block import *
from cache_block import *
from instructions_block import *
from memory_block import *

from cpu import *



backGroundColor = "#1a1a1a"

root = Tk()
root.state("zoomed")
root.resizable(False, False)
root.title("Computer Architecture 2 - 2018109283")
root.configure(bg = backGroundColor)



class LayoutDistribution():
	def __init__(self, root):
		self.controlFrame = Frame(root, bg = backGroundColor)
		self.controlFrame.grid(row = 0, column = 0)

		self.emptyLabel = Label(root, text = "", bg = backGroundColor)
		self.emptyLabel.grid(row = 1, column = 0)

		self.instructionFrame = Frame(root, bg = backGroundColor)
		self.instructionFrame.grid(row = 2, column = 0, sticky = W)

		self.emptyLabel2 = Label(root, text = "", bg = backGroundColor, width = 5)
		self.emptyLabel2.grid(row = 2, column = 1)

		self.cacheFrame = Frame(root, bg = backGroundColor)
		self.cacheFrame.grid(row = 2, column = 2, sticky = E)

		self.emptyLabel3 = Label(root, text = "", bg = backGroundColor)
		self.emptyLabel3.grid(row = 3, column = 0)

		self.emptyLabel4 = Label(root, text = "", bg = backGroundColor)
		self.emptyLabel4.grid(row = 4, column = 0)
		
		self.memoryFrame = Frame(root, bg = backGroundColor)
		self.memoryFrame.grid(row = 5, column = 0, columnspan = 7)



layout = LayoutDistribution(root)


instr = InstructionsBlock(layout.instructionFrame)

cache = CacheBlock(layout.cacheFrame)
cache.startCache()

memory = MemoryBlock(layout.memoryFrame)
memory.startMemory()


################ GUI LOGIC ################
cpu0 = CPU(instr, 0, cache, 0, memory, True)
cpu1 = CPU(instr, 1, cache, 1, memory, True)
cpu2 = CPU(instr, 2, cache, 2, memory, True)
cpu3 = CPU(instr, 3, cache, 3, memory, True)
# cpu0_thread = threading.Thread(target = cpu0.randomInstruction(), args=(1,))
# cpu0_thread.start()


ctrl = ControlBlock(layout.controlFrame, cpu0, cpu1, cpu2, cpu3)

root.mainloop()