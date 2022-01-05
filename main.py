from tkinter import *
root = Tk()


#label widget
mylabel = Label(root,text="Tkinter Program")
#showing it on the screen
mylabel.pack()

canvas = Canvas(width=500,height=500)
canvas.pack()


#looping
root.mainloop()