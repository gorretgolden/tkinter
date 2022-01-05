from tkinter import *
root = Tk()


def mybtn():
    mylabel = Label(root,text= "Welcome" + entry.get()) 
    mylabel.pack()
    
#buttons widget
mybutton = Button(root,text="Click for message",padx=30,command=mybtn,bg="green",fg="white")
#showing it on the screen
mybutton.pack()
#Entry widget
entry = Entry(root,width=50,fg="white",bg="green",borderwidth=3)
#showing it on the screen
entry.pack()
entry.insert(0,"Enter your name")



#looping
root.mainloop()