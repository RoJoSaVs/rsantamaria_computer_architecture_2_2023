from control_block import *
from instructions_block import *
from cache_block import *



root = Tk()
root.state("zoomed")
root.resizable(False, False)
root.title("Computer Architecture 2 - 2018109283")

# width = root.winfo_screenwidth()
# height = root.winfo_screenheight()





class MemoryBlock():
	def __init__(self, root):
		self.memoryLabel = Label(root, text = "Memory")
		self.memoryLabel.grid(row = 0, column = 0, columnspan = 5)




class LayoutDistribution():
	def __init__(self, root):
		self.controlFrame = Frame(root)
		self.controlFrame.grid(row = 0, column = 0)

		self.emptyLabel = Label(root, text = "")
		self.emptyLabel.grid(row = 1, column = 0)

		self.instructionFrame = Frame(root)
		self.instructionFrame.grid(row = 2, column = 0)

		self.emptyLabel2 = Label(root, text = "")
		self.emptyLabel2.grid(row = 0, column = 1, rowspan = 2, columnspan = 2)

		self.cacheFrame = Frame(root)
		self.cacheFrame.grid(row = 0, column = 2)

		self.emptyLabel3 = Label(root, text = "")
		self.emptyLabel3.grid(row = 3, column = 0)

		self.memoryFrame = Frame(root)
		self.memoryFrame.grid(row = 4, column = 0)



layout = LayoutDistribution(root)
ctrl = ControlBlock(layout.controlFrame)
instr = InstructionsBlock(layout.instructionFrame)
cache = CacheBlock(layout.cacheFrame)
memory = MemoryBlock(layout.memoryFrame)

root.mainloop()