from tkinter import *
root = Tk()

grids = Label(root,text="Positioning with grid styling")
grids1 = Label(root,text="Positioning  with grids")
grids.grid(row=2,column=1)
grids1.grid(row=1,column=4)

root.mainloop()