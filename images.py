from tkinter import *
from PIL import Image,ImageTk
root = Tk()
root.title('Images and Icons')

#canvas
cvs = Canvas(root,width=600,height=600)
cvs.grid(columnspan=3)
#needs an icon
# root.iconbitmap('C:\Users\golden\Desktop\image\fruits.jpeg')

my_img = ImageTk.PhotoImage(Image.open("fruits.jpeg"))
my_img1 = ImageTk.PhotoImage(Image.open("orange.jpeg"))
my_img2 = ImageTk.PhotoImage(Image.open("1.jpeg"))
my_img3 = ImageTk.PhotoImage(Image.open("bna.jpeg"))
my_img4 = ImageTk.PhotoImage(Image.open("strw.jpeg"))
my_img5 = ImageTk.PhotoImage(Image.open("fruits.jpeg"))

images= [my_img,my_img1,my_img2,my_img3,my_img4,my_img5]

mylabel = Label(image=my_img)
mylabel.grid(row=0,column=0,columnspan=3)




#looping
root.mainloop()