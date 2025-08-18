# The goal of the project, we will be learning some file handling functions. The things which we do related to the files e.g, creating folders
# deleting files uploading the file, downloading the file etc.. We will be learning how we can upload and download the file

from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
screen=Tk()
screen.geometry("600x600")
screen.title("Uploading files, downloading files, sliders")

# Steps to use it
# 1. First import filedialog at the top
# 2. Then use, asksaveasfilename for downloading the file and then upload and askuploadfilename

def upload():
    #we will use function to upload. upload function allows to select a file from 
    #system. if we want to put it on screen tehn we have to code
    #liek if we want to put image select from system on screen we have to use
    #PIL function and label to give image on screen
    #onl the file mentioned in types will eb allowed to upload
    file=filedialog.askopenfilename(initialdir="/", filetypes=(("Img File", "*.jpg"), ("Imag File", "*.png"), ("Imgg File", "*.jpeg"), ("Text File","*.txt"), ("Python File", "*.py")))
    a=Image.open(file) # in file variable we get image selected from system
    a=a.resize((200, 100))
    a=ImageTk.PhotoImage(a)
    l1=Label(screen, image=a)
    l1.Image=a
    l1.grid(row=3, column=1)

    #if we wneed to upload simple text or python or Html file then we use Label for the same.

def save():
    file=filedialog.asksaveasfile(initialdir="/", filetypes=(("Img File", "*.jpg"), ("Imag File", "*.png"), ("Imgg File", "*.jpeg"), ("Text File","*.txt"), ("Python File", "*.py")))

savebutton=Button(screen, text="Save", fg="black", bg="white", height=3, width=11, command=save)
savebutton.grid(row=2, column=3)
uploadbutton=Button(screen, text="Upload", fg="black", bg="white", height=3, width=11, command=upload)
uploadbutton.grid(row=3, column=3)

# J slider
# J slider means a scale where we set the numbers which we have given range 
s=Scale(screen, from_=1, to=100, orient=HORIZONTAL)
s.grid(row=4, column=1)

def getslidervalue():
    s1=s.get()
    l2.config(text=s1)

l2=Label(screen, fg="black", bg="white", height=3, width=11)
l2.grid(row=5, column=1)
b1=Button(screen, text="Click", fg="black", bg="white", height=3, width=11, command=getslidervalue)
b1.grid(row=5, column=2)

#The goal of the project is what are the values selected on the scale, we get that value and display it as a label on the screen.
mainloop()