from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os

screen=Tk()
screen.configure(bg="white")
screen.title("Notepad")
screen.geometry("600x600")

# We will cretae a menu bar 
# 1. First we will use the menu function to create a box
# 2. We use add_cascade is used to give the name of all the main menus
# 3. then we use add_command to give the name of the items which appear when we click on them 

p1=Text(screen, wrap="word", font=("Arial", 20))
s=Scrollbar(screen, command=p1.yview)# Connects scrollbar with the text box, creating the vertical (y) scrollbar
p1.configure(yscrollcommand=s.set)
p1.pack(side=LEFT, fill=BOTH, expand=TRUE)
file=None

def file1():
    global file 
    file=None
    screen.title("Untitled - Notepad")
    p1.delete(1.0, END)

def open_file():
    global file
    p=filedialog.askopenfilename(defaultextension=".txt", filetypes=(("Img File", "*.jpg"), ("Imag File", "*.png"), ("Imgg File", "*.jpeg"), ("Text File","*.txt"), ("Python File", "*.py")))
    if p: # once we open a file we use insert to put the data from that file to the textbox
        file=p
        with open(p, "r", encoding="utf-8") as f:
            p1.delete(1.0, END)
            p1.insert(END, f.read())
        screen.title(os.path.basename(p)+"- Notepad")    #os.path.basename helps us to get the name of the file    

def save():
    global file
    p=filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Img File", "*.jpg"), ("Imag File", "*.png"), ("Imgg File", "*.jpeg"), ("Text File","*.txt"), ("Python File", "*.py")))
    if p: # once we open a file we use insert to put the data from that file to the textbox
        file=p
        with open(p, "w", encoding="utf-8") as f:
            f.write(p1.get(1.0, END))
        screen.title(os.path.basename(p)+"- Notepad")
    
def exitfile():
    screen.destroy()

def cut():
    p1.event_generate("<<Cut>>")

def copy():
    p1.event_generate("<<Copy>>")

def paste():
    p1.event_generate("<<Paste>>")

# Event_generate is an inbuilt function used to give the functionality of cut, copy and paste 
# Creating the menu bar
menubar=Menu(screen)
filemenu=Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=file1)

filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exitfile)
menubar.add_cascade(label="File", menu=filemenu)

editmenu=Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=cut)
editmenu.add_command(label="Copy", command=copy)
editmenu.add_command(label="Paste", command=paste)
menubar.add_cascade(label="Edit", menu=editmenu)
screen.config(menu=menubar)

mainloop()