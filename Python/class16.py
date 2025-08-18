# Tkinter Library
# Tkinter is a library used to create tui (TUI - graphical user interfix) which means we are able to develop desktop apps.
# Here we create a screen, on the top of it we can create buttons, tables, radio buttons, images, menu bar etc... These are all called as 
# widgets. 
# We can create games but very small types of games. 
#Basic structure for tkinter app
#1. import tkinter
#2. create screen using Tk().syntax : screname=Tk() and set geometry() size of teh screen
#3. Title . syntax : screename.title("Title name")
#4. bg color(optional) : screname.configure(bg="colroname")
#5. mainloop() : its a infinite loop function used in tkinter. always used at the end to make sure screen continues to display
#6. create button, labels, checkbuttons etc.. widgets before mainloop()

#syntax to create any widget :
#variablename=widgetname(screename)
#variabelanme.pack()/grid()/place()

#------------------------------------set positions od widgtes-----------------------------
#three ways
#1. pack() : this set position one after the other in vertical order
#2. grid(row=0, column=0) : sets the position in one line and in another line too. We use rows, columns
#3. place(x=2, y=3) : set position in x, y 

#--------------------------------Style properties for all widgets--------------------------------------------
#1. fg : text color
#2. bg : background color
#3. font : font family, font size
#4. width, height : button, Entry

#Note : we cannot sue all three together. if w ehave strated using pack() w ehave to use that for whole program.


from tkinter import *

screen=Tk()
screen.geometry("600x600")#widthxheight
screen.title("First App")
screen.configure(bg="green")

#widgets
#syntax :variablename=Label(screename, text=)
#pack()
#l1=Label(screen, text="First App", bg="green",fg="white", font=("New times roman", 30))
#l1.pack()

#b1=Button(screen, text="Login", fg="white", bg="red", font=("New times roman", 30))
# b1.pack()

#grid() : put 2 buttons in one line and 2 buttons in next line. to change line change rows. to change position in
#one line chnage column and keep teh row same.
"""b2=Button(screen, text="Login", fg="white", bg="red", font=("New times roman", 30))
b2.grid(row=0, column=0)

b3=Button(screen, text="Login", fg="white", bg="red", font=("New times roman", 30))
b3.grid(row=0, column=1)

b4=Button(screen, text="Login", fg="white", bg="red", font=("New times roman", 30))
b4.grid(row=1, column=0)

b5=Button(screen, text="Login", fg="white", bg="red", font=("New times roman", 30))
b5.grid(row=1, column=1)"""

#place() : x, y 
b2=Button(screen, text="-", fg="white", bg="#ef9c1f", font=("New times roman", 30), width=3, height=1)
b2.place(x=12, y=20)


mainloop()