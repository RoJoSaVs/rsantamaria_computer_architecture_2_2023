# from tkinter import *
from control_mode import *



root = Tk()
root.state("zoomed")
root.resizable(False, False)
root.title("Computer Architecture 2 - 2018109283")

# width = root.winfo_screenwidth()
# height = root.winfo_screenheight()




ctrl = ControlMode(root)
root.mainloop()