from tkinter import *
from PIL import ImageTk, Image
s=Tk()
s.title("images, icons, frames")
#------------------------------icon-----------------------------------
#Steps
#1. to load to store image name in variable use PhotoImage()
#2. if image is .png we use iconphoto() to display on screen. if iamge .ico extemsion then use iconbitmap()

#give image
a=PhotoImage(file="dogimg.png")
#here we pass image to iconphoto to display on screen
s.iconphoto(False,a)

#---------------------------------images-----------------------------------
#Steps :
#1. import PIL library at top. OIL means pillow. isntall pillow using pip in cmd
#2. use function Image.open() to ope image in variable 
#3. resize() to adjust size (optional)
#4. use function ImageTk.PhotoImage() to store image in variable
#5. use label to dipslay on screen. Label is used to give text on screen and image as well.

a=Image.open("dogimg.png")
a=a.resize((200, 100))
a=ImageTk.PhotoImage(a)
l1=Label(s, image=a)
l1.pack()

mainloop()

#--------------------------------Assignment--------------------------------
#create two button, prev and next and two funcion fo both buttons. in one function we do code
#to display one image. and in other function do cod eto dipslay different image. call functions on two buttons.