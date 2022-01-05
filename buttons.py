from tkinter import *
root = Tk()



def mybtn():
    mylabel = Label(root,text="button clicked") 
    mylabel.pack()
    
#buttons widget
mybutton = Button(root,text="Click me",padx=30,command=mybtn,bg="green",fg="white")
#showing it on the screen
mybutton.pack()



#looping
root.mainloop()