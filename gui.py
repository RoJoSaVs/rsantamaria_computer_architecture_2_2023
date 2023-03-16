from tkinter import *



root = Tk()
root.state("zoomed")
root.resizable(False, False)
root.title("Computer Architecture 2 - 2018109283")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
# print(width)

canvas = Canvas(root)

# Draws for CPU representation
canvas.create_rectangle(width * 0.04, height * 0.01, width * 0.24, height * 0.46, outline="#000")
canvas.create_rectangle(width * 0.28, height * 0.01, width * 0.48, height * 0.46, outline="#000")
canvas.create_rectangle(width * 0.52, height * 0.01, width * 0.72, height * 0.46, outline="#000")
canvas.create_rectangle(width * 0.76, height * 0.01, width * 0.96, height * 0.46, outline="#000")


canvas.create_rectangle(width * 0.04, height * 0.5, width * 0.96, height * 0.7, outline="#000") # Bus
canvas.create_rectangle(width * 0.38, height * 0.8, width * 0.62, height * 0.95, outline="#000") # Main memory

canvas.pack(fill=BOTH, expand=1)

root.mainloop()